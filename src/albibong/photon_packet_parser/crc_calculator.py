class CrcCalculator:
    @staticmethod
    def calculate(_bytes, length):
        result = 4294967295
        key = 3988292384

        for i in range(length):
            result ^= _bytes[i]

            for _ in range(8):
                if (result & 1) > 0:
                    result = result >> 1 ^ key
                else:
                    result >>= 1

        return result
