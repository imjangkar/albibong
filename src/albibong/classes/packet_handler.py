import functools
import traceback

from scapy.all import UDP, Packet

from albibong.classes.event_handler import EventHandler
from albibong.classes.logger import Logger
from albibong.classes.world_data import get_world_data
from albibong.photon_packet_parser import (
    EventData,
    OperationRequest,
    OperationResponse,
    PhotonPacketParser,
)

logger = Logger(__name__, ignore_request=True)


def log_payload(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            payload = func(*args, **kwargs)
            logger.log_payload(payload)
        except:
            print(f"ERROR {func.__name__}: {traceback.format_exc()}")

    return wrapper


class PacketHandler:
    def __init__(self):
        self.parser = PhotonPacketParser(
            self.on_event, self.on_request, self.on_response
        )
        self.world_data = get_world_data()
        self.event_handler = EventHandler()

    @log_payload
    def on_event(self, payload: EventData):
        self.event_handler.on_event(self.world_data, payload.parameters)
        return payload

    @log_payload
    def on_request(self, payload: OperationRequest):
        self.event_handler.on_request(self.world_data, payload.parameters)
        return payload

    @log_payload
    def on_response(self, payload: OperationResponse):
        self.event_handler.on_response(self.world_data, payload.parameters)
        return payload

    def handle(self, packet: Packet):
        try:
            payload = packet[UDP].payload.original
            self.parser.handle_payload(payload)
        except Exception as e:
            if type(e) == KeyboardInterrupt:
                raise e

            print(f"ERROR HANDLE: {traceback.format_exc()}")
            logger.log_error_pcap(packet)
