import io
from albibong.photon_packet_parser.message_type import MessageType
from albibong.photon_packet_parser.command_type import CommandType
from albibong.photon_packet_parser.segmented_packet import SegmentedPacket
from albibong.photon_packet_parser.protocol16_deserializer import Protocol16Deserializer
from albibong.photon_packet_parser.crc_calculator import CrcCalculator
from albibong.photon_packet_parser.number_serializer import NumberSerializer

COMMAND_HEADER_LENGTH = 12
PHOTON_HEADER_LENGTH = 12


class PhotonPacketParser:
    def __init__(self, on_event, on_request, on_response):
        self._pending_segments = {}
        self.on_event = on_event
        self.on_request = on_request
        self.on_response = on_response

    # MITIGATOR Challenge Response Packet
    def is_mcr_packet(self, payload):
        signatures = {
            b"\x4d\x43\x52\x48\x33\x31\x31\x30",
            b"\xe9\x71\x2d\xd5\x00\x01\x00\x00",
            b"\xe9\x71\x2d\xd5\x01\x01\x00\x00",
            b"\xe9\x71\x2d\xd5\x11\x01\x00\x00",
        }
        return payload[:8] in signatures

    def handle_payload(self, payload):
        if self.is_mcr_packet(payload):
            return

        payload = io.BytesIO(payload)
        if payload.getbuffer().nbytes < PHOTON_HEADER_LENGTH:
            return

        peer_id = NumberSerializer.deserialize_short(payload)
        flags = payload.read(1)[0]
        command_count = payload.read(1)[0]
        timestamp = NumberSerializer.deserialize_int(payload)
        challenge = NumberSerializer.deserialize_int(payload)

        is_encrypted = flags == 1
        is_crc_enabled = flags == 0xCC

        if is_encrypted:
            return

        if is_crc_enabled:
            offset = payload.tell()
            payload.seek(0)
            crc = NumberSerializer.deserialize_int(payload)

            payload.seek(offset)
            payload = NumberSerializer.serialize_int(0, payload)

            if crc != CrcCalculator.calculate(payload, payload.getbuffer().nbytes):
                return

        for _ in range(command_count):
            self.handle_command(payload)

    def handle_command(self, source: io.BytesIO):
        command_type = source.read(1)[0]
        channel_id = source.read(1)[0]
        command_flags = source.read(1)[0]
        # Skip 1 byte
        source.read(1)
        command_length = NumberSerializer.deserialize_int(source)
        sequence_number = NumberSerializer.deserialize_int(source)
        command_length -= COMMAND_HEADER_LENGTH

        if command_type == CommandType.Disconnect.value:
            return
        elif command_type == CommandType.SendUnreliable.value:
            source.read(4)
            command_length -= 4
            self.handle_send_reliable(source, command_length)
        elif command_type == CommandType.SendReliable.value:
            self.handle_send_reliable(source, command_length)
        elif command_type == CommandType.SendFragment.value:
            self.handle_send_fragment(source, command_length)
        else:
            source.read(command_length)

    def handle_send_reliable(self, source: io.BytesIO, command_length: int):
        # Skip 1 byte
        source.read(1)
        command_length -= 1
        message_type = source.read(1)[0]
        command_length -= 1

        operation_length = command_length
        payload = io.BytesIO(source.read(operation_length))

        if message_type == MessageType.OperationRequest.value:
            request_data = Protocol16Deserializer.deserialize_operation_request(payload)
            self.on_request(request_data)
        elif message_type == MessageType.OperationResponse.value:
            response_data = Protocol16Deserializer.deserialize_operation_response(
                payload
            )
            self.on_response(response_data)
        elif message_type == MessageType.Event.value:
            event_data = Protocol16Deserializer.deserialize_event_data(payload)
            self.on_event(event_data)
        # else:
        #     print("Unknown message type: ", message_type)

    def handle_send_fragment(self, source: io.BytesIO, command_length: int):
        start_sequence_number = NumberSerializer.deserialize_int(source)
        command_length -= 4
        fragment_count = NumberSerializer.deserialize_int(source)
        command_length -= 4
        fragment_number = NumberSerializer.deserialize_int(source)
        command_length -= 4
        total_length = NumberSerializer.deserialize_int(source)
        command_length -= 4
        fragment_offset = NumberSerializer.deserialize_int(source)
        command_length -= 4

        fragment_length = command_length

        self.handle_segmented_payload(
            start_sequence_number,
            total_length,
            fragment_length,
            fragment_offset,
            source,
        )

    def handle_finished_segmented_packet(self, total_payload: bytearray):
        command_length = len(total_payload)
        self.handle_send_reliable(io.BytesIO(total_payload), command_length)

    def handle_segmented_payload(
        self,
        start_sequence_number,
        total_length,
        fragment_length,
        fragment_offset,
        source,
    ):
        segmented_packet = self.get_segmented_packet(
            start_sequence_number, total_length
        )

        for i in range(fragment_length):
            segmented_packet.total_payload[fragment_offset + i] = source.read(1)[0]

        segmented_packet.bytes_written += fragment_length

        if segmented_packet.bytes_written >= segmented_packet.total_length:
            self._pending_segments.pop(start_sequence_number)
            self.handle_finished_segmented_packet(segmented_packet.total_payload)

    def get_segmented_packet(self, start_sequence_number, total_length):
        if start_sequence_number in self._pending_segments:
            return self._pending_segments[start_sequence_number]

        segmented_packet = SegmentedPacket(
            total_length=total_length, total_payload=bytearray(total_length)
        )

        self._pending_segments[start_sequence_number] = segmented_packet

        return segmented_packet
