import io
import struct
import sys
from albibong.photon_packet_parser.protocol16_type import Protocol16Type
from albibong.photon_packet_parser.operation_request import OperationRequest
from albibong.photon_packet_parser.operation_response import OperationResponse
from albibong.photon_packet_parser.event_data import EventData


class Protocol16Deserializer:

    @staticmethod
    def deserialize(input: io.BytesIO, type_code: int):
        if (
            type_code == Protocol16Type.UNKNOWN.value
            or type_code == Protocol16Type.NULL.value
        ):
            return None
        elif type_code == Protocol16Type.DICTIONARY.value:
            return Protocol16Deserializer.deserialize_dictionary(input)
        elif type_code == Protocol16Type.STRINGARRAY.value:
            return Protocol16Deserializer.deserialize_string_array(input)
        elif type_code == Protocol16Type.BYTE.value:
            return Protocol16Deserializer.deserialize_byte(input)
        elif type_code == Protocol16Type.DOUBLE.value:
            return Protocol16Deserializer.deserialize_double(input)
        elif type_code == Protocol16Type.EVENTDATA.value:
            return Protocol16Deserializer.deserialize_event_data(input)
        elif type_code == Protocol16Type.FLOAT.value:
            return Protocol16Deserializer.deserialize_float(input)
        elif type_code == Protocol16Type.INTEGER.value:
            return Protocol16Deserializer.deserialize_integer(input)
        elif type_code == Protocol16Type.HASHTABLE.value:
            return Protocol16Deserializer.deserialize_hash_table(input)
        elif type_code == Protocol16Type.SHORT.value:
            return Protocol16Deserializer.deserialize_short(input)
        elif type_code == Protocol16Type.LONG.value:
            return Protocol16Deserializer.deserialize_long(input)
        elif type_code == Protocol16Type.INTEGERARRAY.value:
            return Protocol16Deserializer.deserialize_integer_array(input)
        elif type_code == Protocol16Type.BOOLEAN.value:
            return Protocol16Deserializer.deserialize_boolean(input)
        elif type_code == Protocol16Type.OPERATIONRESPONSE.value:
            return Protocol16Deserializer.deserialize_operation_response(input)
        elif type_code == Protocol16Type.OPERATIONREQUEST.value:
            return Protocol16Deserializer.deserialize_operation_request(input)
        elif type_code == Protocol16Type.STRING.value:
            return Protocol16Deserializer.deserialize_string(input)
        elif type_code == Protocol16Type.BYTEARRAY.value:
            return Protocol16Deserializer.deserialize_byte_array(input)
        elif type_code == Protocol16Type.ARRAY.value:
            return Protocol16Deserializer.deserialize_array(input)
        elif type_code == Protocol16Type.OBJECTARRAY.value:
            return Protocol16Deserializer.deserialize_object_array(input)
        else:
            raise Exception("Unknown type code: " + str(type_code))

    @staticmethod
    def deserialize_operation_request(input: io.BytesIO):
        code = Protocol16Deserializer.deserialize_byte(input)
        table = Protocol16Deserializer.deserialize_parameter_table(input)
        return OperationRequest(code, table)

    @staticmethod
    def deserialize_operation_response(input: io.BytesIO):
        code = Protocol16Deserializer.deserialize_byte(input)
        return_code = Protocol16Deserializer.deserialize_short(input)
        debug_message = Protocol16Deserializer.deserialize(
            input, Protocol16Deserializer.deserialize_byte(input)
        )
        parameters = Protocol16Deserializer.deserialize_parameter_table(input)
        return OperationResponse(code, return_code, debug_message, parameters)

    @staticmethod
    def deserialize_event_data(input: io.BytesIO):
        code = Protocol16Deserializer.deserialize_byte(input)
        parameters = Protocol16Deserializer.deserialize_parameter_table(input)
        return EventData(code, parameters)

    @staticmethod
    def deserialize_parameter_table(input):
        dictionary_size = Protocol16Deserializer.deserialize_short(input)
        dictionary = {}

        for _ in range(dictionary_size):
            key = Protocol16Deserializer.deserialize_byte(input)
            value_type_code = Protocol16Deserializer.deserialize_byte(input)
            value = Protocol16Deserializer.deserialize(input, value_type_code)
            dictionary[key] = value

        return dictionary

    @staticmethod
    def deserialize_short(input: io.BytesIO):
        buffer = input.read(2)
        return struct.unpack(">h", buffer)[0]

    @staticmethod
    def deserialize_byte(input: io.BytesIO):
        return input.read(1)[0]

    @staticmethod
    def deserialize_boolean(input: io.BytesIO):
        return input.read(1)[0] != 0

    @staticmethod
    def deserialize_integer(input: io.BytesIO):
        buffer = input.read(4)
        return struct.unpack(">i", buffer)[0]

    @staticmethod
    def deserialize_long(input: io.BytesIO):
        buffer = input.read(8)

        if sys.byteorder == "little":
            return struct.unpack(">q", buffer)[0]

        return struct.unpack("<q", buffer)[0]

    @staticmethod
    def deserialize_float(input: io.BytesIO):
        buffer = input.read(4)

        if sys.byteorder == "little":
            return struct.unpack(">f", buffer)[0]

        return struct.unpack("<f", buffer)[0]

    @staticmethod
    def deserialize_double(input: io.BytesIO):
        buffer = input.read(8)

        if sys.byteorder == "little":
            return struct.unpack(">d", buffer)[0]

        return struct.unpack("<d", buffer)[0]

    @staticmethod
    def deserialize_string(input: io.BytesIO):
        string_size = Protocol16Deserializer.deserialize_short(input)

        if string_size == 0:
            return ""

        buffer = input.read(string_size)
        return buffer.decode("utf-8")

    @staticmethod
    def deserialize_byte_array(input: io.BytesIO):
        array_size = Protocol16Deserializer.deserialize_integer(input)

        array = []
        for _ in range(array_size):
            tmp = Protocol16Deserializer.deserialize_byte(input)
            array.append(tmp)

        return array

    @staticmethod
    def deserialize_integer_array(input: io.BytesIO):
        array_size = Protocol16Deserializer.deserialize_integer(input)

        array = []
        for _ in range(array_size):
            tmp = Protocol16Deserializer.deserialize_integer(input)
            array.append(tmp)

        return array

    @staticmethod
    def deserialize_string_array(input: io.BytesIO):
        array_size = Protocol16Deserializer.deserialize_short(input)

        array = []
        for _ in range(array_size):
            tmp = Protocol16Deserializer.deserialize_string(input)
            array.append(tmp)

        return array

    @staticmethod
    def deserialize_object_array(input: io.BytesIO):
        array_size = Protocol16Deserializer.deserialize_short(input)

        array = []
        for _ in range(array_size):
            typeCode = Protocol16Deserializer.deserialize_byte(input)
            tmp = Protocol16Deserializer.deserialize(input, typeCode)
            array.append(tmp)

        return array

    @staticmethod
    def deserialize_array(input: io.BytesIO):
        array_size = Protocol16Deserializer.deserialize_short(input)
        type_code = Protocol16Deserializer.deserialize_byte(input)

        if type_code == Protocol16Type.ARRAY.value:
            result = []
            for _ in range(0, array_size):
                tmp = Protocol16Deserializer.deserialize_array(input)
                result.append(tmp)

            return result
        elif type_code == Protocol16Type.BYTEARRAY.value:
            result = []
            for _ in range(array_size):
                tmp = Protocol16Deserializer.deserialize_byte_array(input)
                result.append(tmp)

            return result
        elif type_code == Protocol16Type.DICTIONARY.value:
            return Protocol16Deserializer.deserialize_dictionary_array(
                input, array_size
            )
        else:
            result = []
            for _ in range(array_size):
                tmp = Protocol16Deserializer.deserialize(input, type_code)
                result.append(tmp)

            return result

    @staticmethod
    def deserialize_dictionary(input: io.BytesIO):
        key_type_code = Protocol16Deserializer.deserialize_byte(input)
        value_type_code = Protocol16Deserializer.deserialize_byte(input)
        dictionary_size = Protocol16Deserializer.deserialize_short(input)
        return Protocol16Deserializer.deserialize_dictionary_elements(
            input, dictionary_size, key_type_code, value_type_code
        )

    @staticmethod
    def deserialize_dictionary_elements(
        input: io.BytesIO,
        dictionary_size: int,
        key_type_code: int,
        value_type_code: int,
    ):
        output = {}
        for _ in range(dictionary_size):
            key = Protocol16Deserializer.deserialize(
                input,
                (
                    Protocol16Deserializer.deserialize_byte(input)
                    if key_type_code == 0 or key_type_code == 42
                    else key_type_code
                ),
            )
            value = Protocol16Deserializer.deserialize(
                input,
                (
                    Protocol16Deserializer.deserialize_byte(input)
                    if value_type_code == 0 or value_type_code == 42
                    else value_type_code
                ),
            )
            output[key] = value

        return output

    @staticmethod
    def deserialize_dictionary_array(input: io.BytesIO, size: int):
        key_type_code = Protocol16Deserializer.deserialize_byte(input)
        value_type_code = Protocol16Deserializer.deserialize_byte(input)
        output = []

        for _ in range(size):
            dictionary_size = Protocol16Deserializer.deserialize_short(input)

            dictionary = {}
            for _ in range(dictionary_size):
                key = None
                if key_type_code > 0:
                    key = Protocol16Deserializer.deserialize(input, key_type_code)
                else:
                    next_key_type_code = Protocol16Deserializer.deserialize_byte(input)
                    key = Protocol16Deserializer.deserialize(input, next_key_type_code)

                value = None
                if value_type_code > 0:
                    value = Protocol16Deserializer.deserialize(input, value_type_code)
                else:
                    next_value_type_code = Protocol16Deserializer.deserialize_byte(
                        input
                    )
                    value = Protocol16Deserializer.deserialize(
                        input, next_value_type_code
                    )

                dictionary[key] = value

            output.append(dictionary)

        return output

    @staticmethod
    def deserialize_hash_table(input: io.BytesIO):
        size = Protocol16Deserializer.deserialize_short(input)
        return Protocol16Deserializer.deserialize_dictionary_elements(
            input, size, Protocol16Type.UNKNOWN, Protocol16Type.UNKNOWN
        )
