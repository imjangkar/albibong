"""Regression tests for the Protocol18 (GpBinary v18) deserializer.

The hex payloads below are real Albion message bodies captured from live
traffic (the bytes that follow the [0xF3 signature][message-type] framing).
Run with:  PYTHONPATH=src python -m pytest tests/  (or: python tests/test_protocol18_deserializer.py)
"""

import io

from albibong.photon_packet_parser.protocol18_deserializer import (
    Protocol18Deserializer as P18,
)

# A NEW_CHARACTER event (parameters[252] == 29) for player "Fosterchef".
NEW_CHARACTER = (
    "01 26 00 0a 84 85 1d 01 07 0a 46 6f 73 74 65 72 63 68 65 66 02 0b 04 05 43 "
    "05 05 00 01 00 03 06 43 05 00 03 08 00 05 07 43 10 b2 cc ca 15 d4 63 93 4b "
    "97 2f f3 f8 09 a0 bc de 0a 07 00 0b 1e 0c 1e 0d 07 00 10 43 08 62 63 31 34 "
    "b7 ab 48 d3 11 43 08 62 63 31 34 b7 ab 48 d3 12 09 d6 95 a5 05 14 05 66 66 "
    "f6 40 16 05 00 20 d1 44 17 05 00 20 d1 44 19 05 7c cc 23 42 1a 09 d6 95 a5 "
    "05 1b 05 00 00 3a 43 1c 05 00 00 3a 43 1e 05 0e de 1d 40 1f 09 d6 95 a5 05 "
    "20 05 00 00 86 43 21 05 00 00 86 43 23 05 1f 85 2b 40 24 09 d6 95 a5 05 25 "
    "05 56 1b b8 42 26 09 d6 95 a5 05 27 03 04 28 44 0a 1d 21 cc 07 3b 0d b6 0f "
    "71 0d 0e 0b 93 09 9b 0b 00 00 00 00 2b 44 0e 05 0e 1b 0e 1e 0e 3f 0f a6 0f "
    "dd 0f ff ff ff ff ff ff ff ff ff ff ff ff ff ff 34 10 33 07 00 35 22 36 22 "
    "37 44 07 ff ff ff ff ff ff ff ff ff ff ff ff ff ff 38 22 3f 1e fc 04 1d 00"
)

# An OperationResponse: code 1, return 0, null debug, params {255: 61, 253: 52}.
OPERATION_RESPONSE = "01 00 00 08 02 ff 0b 3d fd 04 34 00"

# A frequent movement event: params {0: <compressed long>, 1: <30-byte array>}.
MOVE_EVENT = (
    "03 02 00 0a f4 99 17 01 43 1e 03 85 48 f4 c5 88 c4 de 08 45 c1 a4 27 23 b6 "
    "c4 e8 09 00 00 b0 40 8c a4 9e 27 38 89 52 e9"
)


def _stream(hex_str):
    return io.BytesIO(bytes.fromhex(hex_str))


def _assert_fully_consumed(stream, body_len):
    assert stream.tell() == body_len, (
        f"expected to consume {body_len} bytes, consumed {stream.tell()}"
    )


def test_new_character_event_decodes_player():
    body = bytes.fromhex(NEW_CHARACTER)
    stream = io.BytesIO(body)
    event = P18.deserialize_event_data(stream)

    _assert_fully_consumed(stream, len(body))
    assert event.parameters[252] == 29  # NEW_CHARACTER
    assert event.parameters[1] == "Fosterchef"  # username (string)
    assert isinstance(event.parameters[7], list) and len(event.parameters[7]) == 16  # uuid bytes
    assert isinstance(event.parameters[0], int)  # entity id


def test_operation_response_decodes():
    body = bytes.fromhex(OPERATION_RESPONSE)
    stream = io.BytesIO(body)
    response = P18.deserialize_operation_response(stream)

    _assert_fully_consumed(stream, len(body))
    assert response.operation_code == 1
    assert response.return_code == 0
    assert response.parameters[253] == 52  # short, little-endian
    assert response.parameters[255] == 61  # Int1


def test_move_event_decodes():
    body = bytes.fromhex(MOVE_EVENT)
    stream = io.BytesIO(body)
    event = P18.deserialize_event_data(stream)

    _assert_fully_consumed(stream, len(body))
    assert event.code == 3
    assert isinstance(event.parameters[0], int)  # compressed long
    assert isinstance(event.parameters[1], list) and len(event.parameters[1]) == 30  # byte array


def test_zigzag_varint_roundtrip():
    # compressed int: 0x00 -> 0, 0x01 -> -1, 0x02 -> 1, 0x03 -> -2
    assert P18._read_compressed_int32(io.BytesIO(b"\x00")) == 0
    assert P18._read_compressed_int32(io.BytesIO(b"\x01")) == -1
    assert P18._read_compressed_int32(io.BytesIO(b"\x02")) == 1
    assert P18._read_compressed_int32(io.BytesIO(b"\x03")) == -2
    # multi-byte varint: 0x96 0x01 -> uint 150 -> zigzag 75
    assert P18._read_compressed_int32(io.BytesIO(b"\x96\x01")) == 75


def test_little_endian_short():
    assert P18._deserialize_short(io.BytesIO(b"\x34\x00")) == 52
    assert P18._deserialize_short(io.BytesIO(b"\x00\x01")) == 256


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print(f"PASS {name}")
    print("All Protocol18 tests passed.")
