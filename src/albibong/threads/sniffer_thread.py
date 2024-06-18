import threading

from scapy.all import AsyncSniffer

from albibong.classes.logger import Logger

logger = Logger(__name__, stdout=True, log_to_file=False)


class SnifferThread(threading.Thread):
    def __init__(self, name, out_queue, sentinel):
        super().__init__()
        self.name = name
        self.out_queue = out_queue
        self.sentinel = sentinel
        self.sniffer = AsyncSniffer(filter="udp and port 5056", prn=self.push_packet)

    def push_packet(self, packet):
        self.out_queue.put(packet)

    def run(self):
        logger.info(f"Thread {self.name} started")
        self.sniffer.start()

    def stop(self):
        logger.info(f"Thread {self.name} stopped")
        self.sniffer.stop()
        self.out_queue.put(self.sentinel)
