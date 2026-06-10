"""Photon GpBinary v18 (Protocol18) deserializer.

Albion Online migrated its Photon payload serialization from Protocol16 to
Protocol18 (GpBinary v18). The transport layer (commands, 0xF3 signature,
message types) is unchanged, but the value serialization differs completely:

  * the parameter-table count is a single byte (not a 2-byte short),
  * shorts/ints are little-endian,
  * integers/longs are zig-zag varint encoded,
  * the type-code table is different (see Protocol18Type).

Ported from the actively-maintained reference implementation in
Triky313/AlbionOnline-StatisticsAnalysis (StatisticsAnalysisTool.Protocol18).

Returned Python types mirror what the old Protocol16 deserializer produced so
the existing event handlers keep working: int / float / str / list / dict /
bool / None, and byte arrays as a list of ints.
"""

import io
import struct

from albibong.photon_packet_parser.event_data import EventData
from albibong.photon_packet_parser.operation_request import OperationRequest
from albibong.photon_packet_parser.operation_response import OperationResponse


class Protocol18Type:
    Unknown = 0
    Boolean = 2
    Byte = 3
    Short = 4
    Float = 5
    Double = 6
    String = 7
    Null = 8
    CompressedInt = 9
    CompressedLong = 10
    Int1 = 11
    Int1Negative = 12
    Int2 = 13
    Int2Negative = 14
    Long1 = 15
    Long1Negative = 16
    Long2 = 17
    Long2Negative = 18
    Custom = 19
    Dictionary = 20
    Hashtable = 21
    ObjectArray = 23
    OperationRequest = 24
    OperationResponse = 25
    EventData = 26
    BooleanFalse = 27
    BooleanTrue = 28
    ShortZero = 29
    IntZero = 30
    LongZero = 31
    FloatZero = 32
    DoubleZero = 33
    ByteZero = 34
    Array = 64
    BooleanArray = 66
    ByteArray = 67
    ShortArray = 68
    FloatArray = 69
    DoubleArray = 70
    StringArray = 71
    CompressedIntArray = 73
    CompressedLongArray = 74
    CustomTypeArray = 83
    DictionaryArray = 84
    HashtableArray = 85
    CustomTypeSlim = 128


CUSTOM_TYPE_SLIM = 128
MAX_SLIM_CUSTOM_TYPE_CODE = 228


def _read_byte(stream: io.BytesIO) -> int:
    b = stream.read(1)
    if len(b) != 1:
        raise EOFError("Protocol18: unexpected end of payload")
    return b[0]


def _read_exact(stream: io.BytesIO, n: int) -> bytes:
    data = stream.read(n)
    if len(data) != n:
        raise EOFError(f"Protocol18: expected {n} bytes, got {len(data)}")
    return data


class Protocol18Deserializer:

    # ---- top-level message structures -------------------------------------

    @staticmethod
    def deserialize_event_data(stream: io.BytesIO) -> EventData:
        code = _read_byte(stream)
        parameters = Protocol18Deserializer._deserialize_parameter_table(stream)
        return EventData(code, parameters)

    @staticmethod
    def deserialize_operation_request(stream: io.BytesIO) -> OperationRequest:
        operation_code = _read_byte(stream)
        parameters = Protocol18Deserializer._deserialize_parameter_table(stream)
        return OperationRequest(operation_code, parameters)

    @staticmethod
    def deserialize_operation_response(stream: io.BytesIO) -> OperationResponse:
        operation_code = _read_byte(stream)
        return_code = Protocol18Deserializer._deserialize_short(stream)
        debug_message = Protocol18Deserializer.deserialize(stream, _read_byte(stream))
        if not isinstance(debug_message, str):
            debug_message = ""
        parameters = Protocol18Deserializer._deserialize_parameter_table(stream)
        return OperationResponse(operation_code, return_code, debug_message, parameters)

    # ---- value dispatch ----------------------------------------------------

    @staticmethod
    def deserialize(stream: io.BytesIO, type_code: int = None):
        if type_code is None:
            type_code = _read_byte(stream)

        if CUSTOM_TYPE_SLIM <= type_code <= MAX_SLIM_CUSTOM_TYPE_CODE:
            return Protocol18Deserializer._deserialize_custom_type(stream, type_code)

        d = Protocol18Deserializer
        T = Protocol18Type
        handler = _DISPATCH.get(type_code)
        if handler is None:
            raise ValueError(f"Protocol18 type code {type_code} is not supported")
        return handler(d, stream)

    # ---- scalars -----------------------------------------------------------

    @staticmethod
    def _deserialize_short(stream: io.BytesIO) -> int:
        return struct.unpack("<h", _read_exact(stream, 2))[0]

    @staticmethod
    def _deserialize_ushort(stream: io.BytesIO) -> int:
        return struct.unpack("<H", _read_exact(stream, 2))[0]

    @staticmethod
    def _deserialize_float(stream: io.BytesIO) -> float:
        return struct.unpack("<f", _read_exact(stream, 4))[0]

    @staticmethod
    def _deserialize_double(stream: io.BytesIO) -> float:
        return struct.unpack("<d", _read_exact(stream, 8))[0]

    @staticmethod
    def _deserialize_boolean(stream: io.BytesIO) -> bool:
        return _read_byte(stream) != 0

    @staticmethod
    def _deserialize_string(stream: io.BytesIO) -> str:
        length = Protocol18Deserializer._read_compressed_uint32(stream)
        if length == 0:
            return ""
        return _read_exact(stream, length).decode("utf-8", errors="replace")

    # ---- varints -----------------------------------------------------------

    @staticmethod
    def _read_compressed_uint32(stream: io.BytesIO) -> int:
        value = 0
        shift = 0
        while shift != 35:
            current = _read_byte(stream)
            value |= (current & 0x7F) << shift
            shift += 7
            if (current & 0x80) == 0:
                break
        return value & 0xFFFFFFFF

    @staticmethod
    def _read_compressed_uint64(stream: io.BytesIO) -> int:
        value = 0
        shift = 0
        while shift != 70:
            current = _read_byte(stream)
            value |= (current & 0x7F) << shift
            shift += 7
            if (current & 0x80) == 0:
                break
        return value & 0xFFFFFFFFFFFFFFFF

    @staticmethod
    def _read_compressed_int32(stream: io.BytesIO) -> int:
        v = Protocol18Deserializer._read_compressed_uint32(stream)
        return (v >> 1) ^ (-(v & 1))

    @staticmethod
    def _read_compressed_int64(stream: io.BytesIO) -> int:
        v = Protocol18Deserializer._read_compressed_uint64(stream)
        return (v >> 1) ^ (-(v & 1))

    @staticmethod
    def _read_int1(stream, negative):
        v = _read_byte(stream)
        return -v if negative else v

    @staticmethod
    def _read_int2(stream, negative):
        v = Protocol18Deserializer._deserialize_ushort(stream)
        return -v if negative else v

    # ---- arrays ------------------------------------------------------------

    @staticmethod
    def _deserialize_byte_array(stream: io.BytesIO) -> list:
        length = Protocol18Deserializer._read_compressed_uint32(stream)
        return list(_read_exact(stream, length))

    @staticmethod
    def _deserialize_short_array(stream: io.BytesIO) -> list:
        length = Protocol18Deserializer._read_compressed_uint32(stream)
        return [Protocol18Deserializer._deserialize_short(stream) for _ in range(length)]

    @staticmethod
    def _deserialize_float_array(stream: io.BytesIO) -> list:
        length = Protocol18Deserializer._read_compressed_uint32(stream)
        return [Protocol18Deserializer._deserialize_float(stream) for _ in range(length)]

    @staticmethod
    def _deserialize_double_array(stream: io.BytesIO) -> list:
        length = Protocol18Deserializer._read_compressed_uint32(stream)
        return [Protocol18Deserializer._deserialize_double(stream) for _ in range(length)]

    @staticmethod
    def _deserialize_string_array(stream: io.BytesIO) -> list:
        length = Protocol18Deserializer._read_compressed_uint32(stream)
        return [Protocol18Deserializer._deserialize_string(stream) for _ in range(length)]

    @staticmethod
    def _deserialize_compressed_int_array(stream: io.BytesIO) -> list:
        length = Protocol18Deserializer._read_compressed_uint32(stream)
        return [
            Protocol18Deserializer._read_compressed_int32(stream) for _ in range(length)
        ]

    @staticmethod
    def _deserialize_compressed_long_array(stream: io.BytesIO) -> list:
        length = Protocol18Deserializer._read_compressed_uint32(stream)
        return [
            Protocol18Deserializer._read_compressed_int64(stream) for _ in range(length)
        ]

    @staticmethod
    def _deserialize_boolean_array(stream: io.BytesIO) -> list:
        length = Protocol18Deserializer._read_compressed_uint32(stream)
        result = [False] * length
        full_bytes = length // 8
        index = 0
        for _ in range(full_bytes):
            value = _read_byte(stream)
            for bit in range(8):
                result[index] = (value & (1 << bit)) != 0
                index += 1
        if index < length:
            value = _read_byte(stream)
            bit = 0
            while index < length:
                result[index] = (value & (1 << bit)) != 0
                index += 1
                bit += 1
        return result

    @staticmethod
    def _deserialize_object_array(stream: io.BytesIO) -> list:
        length = Protocol18Deserializer._read_compressed_uint32(stream)
        return [Protocol18Deserializer.deserialize(stream) for _ in range(length)]

    @staticmethod
    def _deserialize_array_in_array(stream: io.BytesIO) -> list:
        length = Protocol18Deserializer._read_compressed_uint32(stream)
        return [Protocol18Deserializer.deserialize(stream) for _ in range(length)]

    # ---- dictionaries / hashtables ----------------------------------------

    @staticmethod
    def _deserialize_hashtable(stream: io.BytesIO) -> dict:
        size = Protocol18Deserializer._read_compressed_uint32(stream)
        out = {}
        for _ in range(size):
            key = Protocol18Deserializer.deserialize(stream)
            value = Protocol18Deserializer.deserialize(stream)
            try:
                out[key] = value
            except TypeError:
                out[str(key)] = value
        return out

    @staticmethod
    def _read_dictionary_type(stream: io.BytesIO):
        """Read a dictionary's key/value type descriptor, consuming any nested
        type bytes, mirroring the reference DeserializeDictionaryType."""
        key_type = _read_byte(stream)
        value_type = _read_byte(stream)
        if value_type == Protocol18Type.Dictionary:
            Protocol18Deserializer._read_dictionary_type(stream)
        elif value_type == Protocol18Type.Array:
            tc = _read_byte(stream)
            while tc == Protocol18Type.Array:
                tc = _read_byte(stream)
            value_type = Protocol18Type.Unknown
        return key_type, value_type

    @staticmethod
    def _deserialize_dictionary_elements(stream, key_type, value_type) -> dict:
        size = Protocol18Deserializer._read_compressed_uint32(stream)
        out = {}
        for _ in range(size):
            key = (
                Protocol18Deserializer.deserialize(stream)
                if key_type == Protocol18Type.Unknown
                else Protocol18Deserializer.deserialize(stream, key_type)
            )
            value = (
                Protocol18Deserializer.deserialize(stream)
                if value_type == Protocol18Type.Unknown
                else Protocol18Deserializer.deserialize(stream, value_type)
            )
            try:
                out[key] = value
            except TypeError:
                out[str(key)] = value
        return out

    @staticmethod
    def _deserialize_dictionary(stream: io.BytesIO) -> dict:
        key_type, value_type = Protocol18Deserializer._read_dictionary_type(stream)
        return Protocol18Deserializer._deserialize_dictionary_elements(
            stream, key_type, value_type
        )

    @staticmethod
    def _deserialize_dictionary_array(stream: io.BytesIO) -> list:
        key_type, value_type = Protocol18Deserializer._read_dictionary_type(stream)
        length = Protocol18Deserializer._read_compressed_uint32(stream)
        return [
            Protocol18Deserializer._deserialize_dictionary_elements(
                stream, key_type, value_type
            )
            for _ in range(length)
        ]

    @staticmethod
    def _deserialize_hashtable_array(stream: io.BytesIO) -> list:
        length = Protocol18Deserializer._read_compressed_uint32(stream)
        return [
            Protocol18Deserializer._deserialize_hashtable(stream) for _ in range(length)
        ]

    # ---- custom types ------------------------------------------------------

    @staticmethod
    def _deserialize_custom_type(stream: io.BytesIO, slim_type_code: int = 0):
        if slim_type_code == 0:
            _read_byte(stream)  # custom type code (unused)
        length = Protocol18Deserializer._read_compressed_uint32(stream)
        return list(_read_exact(stream, length))

    @staticmethod
    def _deserialize_custom_type_array(stream: io.BytesIO) -> list:
        length = Protocol18Deserializer._read_compressed_uint32(stream)
        _read_byte(stream)  # element custom type code (unused)
        result = []
        for _ in range(length):
            data_length = Protocol18Deserializer._read_compressed_uint32(stream)
            result.append(list(_read_exact(stream, data_length)))
        return result

    # ---- parameter table ---------------------------------------------------

    @staticmethod
    def _deserialize_parameter_table(stream: io.BytesIO) -> dict:
        size = _read_byte(stream)
        parameters = {}
        for _ in range(size):
            key = _read_byte(stream)
            value_type_code = _read_byte(stream)
            parameters[key] = Protocol18Deserializer.deserialize(stream, value_type_code)
        return parameters


# Dispatch table mapping a Protocol18 type code to a handler taking
# (Protocol18Deserializer, stream). Defined after the class so the methods exist.
_T = Protocol18Type
_DISPATCH = {
    _T.Boolean: lambda d, s: d._deserialize_boolean(s),
    _T.Byte: lambda d, s: _read_byte(s),
    _T.Short: lambda d, s: d._deserialize_short(s),
    _T.Float: lambda d, s: d._deserialize_float(s),
    _T.Double: lambda d, s: d._deserialize_double(s),
    _T.String: lambda d, s: d._deserialize_string(s),
    _T.Null: lambda d, s: None,
    _T.CompressedInt: lambda d, s: d._read_compressed_int32(s),
    _T.CompressedLong: lambda d, s: d._read_compressed_int64(s),
    _T.Int1: lambda d, s: d._read_int1(s, False),
    _T.Int1Negative: lambda d, s: d._read_int1(s, True),
    _T.Int2: lambda d, s: d._read_int2(s, False),
    _T.Int2Negative: lambda d, s: d._read_int2(s, True),
    _T.Long1: lambda d, s: d._read_int1(s, False),
    _T.Long1Negative: lambda d, s: d._read_int1(s, True),
    _T.Long2: lambda d, s: d._read_int2(s, False),
    _T.Long2Negative: lambda d, s: d._read_int2(s, True),
    _T.Custom: lambda d, s: d._deserialize_custom_type(s),
    _T.Dictionary: lambda d, s: d._deserialize_dictionary(s),
    _T.Hashtable: lambda d, s: d._deserialize_hashtable(s),
    _T.ObjectArray: lambda d, s: d._deserialize_object_array(s),
    _T.OperationRequest: lambda d, s: d.deserialize_operation_request(s),
    _T.OperationResponse: lambda d, s: d.deserialize_operation_response(s),
    _T.EventData: lambda d, s: d.deserialize_event_data(s),
    _T.BooleanFalse: lambda d, s: False,
    _T.BooleanTrue: lambda d, s: True,
    _T.ShortZero: lambda d, s: 0,
    _T.IntZero: lambda d, s: 0,
    _T.LongZero: lambda d, s: 0,
    _T.FloatZero: lambda d, s: 0.0,
    _T.DoubleZero: lambda d, s: 0.0,
    _T.ByteZero: lambda d, s: 0,
    _T.Array: lambda d, s: d._deserialize_array_in_array(s),
    _T.BooleanArray: lambda d, s: d._deserialize_boolean_array(s),
    _T.ByteArray: lambda d, s: d._deserialize_byte_array(s),
    _T.ShortArray: lambda d, s: d._deserialize_short_array(s),
    _T.FloatArray: lambda d, s: d._deserialize_float_array(s),
    _T.DoubleArray: lambda d, s: d._deserialize_double_array(s),
    _T.StringArray: lambda d, s: d._deserialize_string_array(s),
    _T.CompressedIntArray: lambda d, s: d._deserialize_compressed_int_array(s),
    _T.CompressedLongArray: lambda d, s: d._deserialize_compressed_long_array(s),
    _T.CustomTypeArray: lambda d, s: d._deserialize_custom_type_array(s),
    _T.DictionaryArray: lambda d, s: d._deserialize_dictionary_array(s),
    _T.HashtableArray: lambda d, s: d._deserialize_hashtable_array(s),
}
