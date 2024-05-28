import threading
from albibong.classes.logger import Logger
from albibong.classes.packet_handler import PacketHandler

logger = Logger(__name__, stdout=True, log_to_file=False)


class PacketHandlerThread(threading.Thread):
    def __init__(self, name, in_queue, sentinel):
        super().__init__()
        self.name = name
        self.in_queue = in_queue
        self.sentinel = sentinel
        self.packet_handler = PacketHandler()
        self.stop_event = threading.Event()

    def run(self):
        logger.info(f"Thread {self.name} started")
        while True:
            if self.stop_event.is_set():
                break

            packet = self.in_queue.get()
            if packet == self.sentinel:
                logger.info(f"Thread {self.name} stopped")
                break

            self.packet_handler.handle(packet)

    def stop(self):
        logger.info(f"Thread {self.name} stopped")
        self.stop_event.set()
