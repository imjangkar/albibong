from datetime import datetime
import queue
import random
import socket
import sys
from time import sleep
import uuid

import webview
from scapy.all import rdpcap

from albibong.classes.dungeon import Dungeon
from albibong.classes.logger import Logger
from albibong.classes.packet_handler import PacketHandler
from albibong.threads.http_server import HttpServerThread
from albibong.threads.packet_handler_thread import PacketHandlerThread
from albibong.threads.sniffer_thread import SnifferThread
from albibong.threads.websocket_server import get_ws_server
from albibong.models.models import db

logger = Logger(__name__, stdout=True, log_to_file=False)
PORT = random.randrange(8500, 8999)


def read_pcap(path):
    packet_handler = PacketHandler()
    scapy_cap = rdpcap(path)
    for packet in scapy_cap:
        packet_handler.handle(packet)


def sniff(useWebview):
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

    # --- start trial db ---

    db.connect()
    db.create_tables([Dungeon])

    obj: Dungeon = Dungeon(
        type="DUNGEON_SAFEAREA",
        name=f"DG {random.randint(1,100)}",
    )

    obj.update_fame(
        {
            0: 48,
            1: 4991558844254,
            2: 2373972,
            3: 1,
            4: 20624,
            5: True,
            6: 0.36000001430511475,
            252: 82,
        }
    )

    obj.update_loot({0: 48, 2: "imjangkar", 3: True, 5: 251973, 252: 271})

    obj.update_re_spec({0: [0, 94541807877, 0, 0, 0], 1: 1, 2: 700000, 252: 84})

    sleep(2)

    obj.set_end_time()

    # print(f"Data baru:\n{Dungeon.serialize(obj)}")

    obj.save(force_insert=True)

    # --- end trial db ---

    if useWebview:

        sock = socket.socket()
        sock.bind(("", 0))
        port = sock.getsockname()[1]
        sock.close()

        http_server = HttpServerThread(name="http_server", port=port)
        http_server.start()

        window = webview.create_window(
            "Albibong",
            url=f"http://localhost:{port}/",
            width=1280,
            height=720,
            zoomable=True,
        )

        def on_closing():
            c.stop()
            p.stop()
            ws_server.stop()
            http_server.stop()
            db.close()

        window.events.closing += on_closing

        webview.start()
    else:
        try:
            while True:
                sleep(100)
        except KeyboardInterrupt as e:
            p.stop()
            ws_server.stop()


def main(useWebview=True):
    if len(sys.argv) > 1:
        ws_server = get_ws_server()
        ws_server.start()

        read_pcap(sys.argv[1])
    else:
        sniff(useWebview)
