import os
import threading
from time import sleep

from scapy.all import AsyncSniffer, wrpcapng

from albibong.classes.logger import Logger
from albibong.threads.websocket_server import send_event

home_dir = os.path.expanduser("~")
pcap_file = home_dir + "/Albibong/Debug/debug.pcapng"

logger = Logger(__name__, stdout=True, log_to_file=False)


class SnifferThread(threading.Thread):
    def __init__(self, name, out_queue, sentinel, is_debug=False):
        super().__init__()
        self.name = name
        self.out_queue = out_queue
        self.sentinel = sentinel
        self.is_debug = is_debug
        self.sniffer = AsyncSniffer(filter="udp and port 5056", prn=self.push_packet)
        self.packet_counter = 0
        self.timer_exit = threading.Event()
        self.all_packets = []

    def push_packet(self, packet):
        self.out_queue.put(packet)
        self.all_packets.append(packet)
        self.packet_counter += 1

    def run(self):
        logger.info(f"Thread {self.name} started")
        self.sniffer.start()
        timer = threading.Thread(target=self.start_timer, args=[5], daemon=True)
        timer.run()

    def stop(self):
        logger.info(f"Thread {self.name} stopped")
        self.sniffer.stop()
        self.out_queue.put(self.sentinel)
        self.quit_timer()
        if self.is_debug:
            wrpcapng(pcap_file, self.all_packets)

    def start_timer(self, seconds):
        while not self.timer_exit.is_set():
            self.timer_exit.wait(seconds)

            if self.packet_counter > 0:
                msg = {
                    "type": "health_check",
                    "payload": {"status": "passed", "message": "Passed"},
                }
            else:
                msg = {
                    "type": "health_check",
                    "payload": {"status": "failed", "message": "No Packets Received"},
                }
            send_event(msg)
            self.packet_counter = 0

    def quit_timer(self):
        self.timer_exit.set()
