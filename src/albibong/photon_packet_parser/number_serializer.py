import io
import struct


class NumberSerializer:
    @staticmethod
    def deserialize_int(source: io.BytesIO):
        buffer = source.read(4)
        return struct.unpack(">i", buffer)[0]

    @staticmethod
    def deserialize_short(source: io.BytesIO):
        buffer = source.read(2)
        return struct.unpack(">h", buffer)[0]

    @staticmethod
    def serialize_int(value, target: io.BytesIO):
        target.write(value >> 24)
        target.write(value >> 16)
        target.write(value >> 8)
        target.write(value)
        return target
