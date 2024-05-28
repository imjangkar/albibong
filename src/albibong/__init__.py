import queue
import sys
from time import sleep

import webview
from scapy.all import rdpcap

from albibong.classes.logger import Logger
from albibong.classes.packet_handler import PacketHandler
from albibong.threads.http_server import HttpServerThread
from albibong.threads.packet_handler_thread import PacketHandlerThread
from albibong.threads.sniffer_thread import SnifferThread
from albibong.threads.websocket_server import get_ws_server

logger = Logger(__name__, stdout=True, log_to_file=False)


def read_pcap(path):
    packet_handler = PacketHandler()
    scapy_cap = rdpcap(path)
    for packet in scapy_cap:
        packet_handler.handle(packet)


def sniff():
    _sentinel = object()
    packet_queue = queue.Queue()

    p = SnifferThread(name="sniffer", out_queue=packet_queue, sentinel=_sentinel)

    c = PacketHandlerThread(
        name="packet_handler",
        in_queue=packet_queue,
        sentinel=_sentinel,
    )

    p.start()
    c.start()

    ws_server = get_ws_server()
    ws_server.start()

    http_server = HttpServerThread(name="http_server")
    http_server.start()

    # sleep(0.25)
    # with open("../gui/dist/index.html", "r") as html:
    window = webview.create_window(
        "Albibong",
        # "../../gui/dist/index.html",
        url="http://localhost:8000/",
        width=1280,
        height=720,
        zoomable=True,
    )

    def on_closing():
        c.stop()
        p.stop()
        ws_server.stop()
        http_server.stop()

    window.events.closing += on_closing

    webview.start()


def main():
    if len(sys.argv) > 1:
        ws_server = get_ws_server()
        ws_server.start()

        http_server = HttpServerThread(name="http_server")
        http_server.start()

        read_pcap(sys.argv[1])
    else:
        sniff()
