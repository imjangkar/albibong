from uuid import UUID


class Utils:

    @staticmethod
    def convert_int_arr_to_uuid(arr):
        b = bytes(arr)
        return UUID(bytes=b)
