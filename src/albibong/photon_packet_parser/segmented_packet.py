class SegmentedPacket:
    def __init__(self, total_length=0, bytes_written=0, total_payload=bytearray(0)):
        self.total_length = total_length
        self.bytes_written = bytes_written
        self.total_payload = total_payload
