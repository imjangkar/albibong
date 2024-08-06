import json
import os
import queue
import random
import socket
import sys
import uuid
from datetime import datetime, timedelta
from pathlib import Path
from time import sleep

import webview
from scapy.all import rdpcap

from albibong.classes.dungeon import Dungeon
from albibong.classes.logger import Logger
from albibong.classes.packet_handler import PacketHandler
from albibong.models.models import db
from albibong.threads.http_server import HttpServerThread
from albibong.threads.packet_handler_thread import PacketHandlerThread
from albibong.threads.sniffer_thread import SnifferThread
from albibong.threads.websocket_server import get_ws_server

logger = Logger(__name__, stdout=True, log_to_file=False)
PORT = random.randrange(8500, 8999)

home_dir = os.path.expanduser("~")
JSON_DB = f"{home_dir}/Albibong/list_dungeon.json"
SQLITE_DB = f"{home_dir}/Albibong/Albibong.db"


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

    def get_end_time(str, start_time):
        timer = str.split(":")
        seconds = int(timer[0]) * 3600 + int(timer[1]) * 60 + int(timer[2])
        return timedelta(seconds=seconds) + start_time

    if Path(SQLITE_DB).is_file() == False:
        if Path(JSON_DB).is_file() == True:
            # convert json db to sqlite db
            db.connect()
            db.create_tables([Dungeon])
            json_data = json.load(open(JSON_DB))
            for dungeon in json_data:
                start_time = datetime.strptime(
                    dungeon["date_time"], "%a %d %b %Y, %I:%M%p"
                )
                Dungeon.create(
                    type=dungeon["type"],
                    name=dungeon["name"],
                    tier=dungeon["tier"],
                    fame=dungeon["fame"],
                    silver=dungeon["silver"],
                    re_spec=dungeon["re_spec"],
                    start_time=start_time,
                    end_time=get_end_time(dungeon["time_elapsed"], start_time),
                )
            Path(JSON_DB).unlink()

    db.connect(reuse_if_open=True)
    db.create_tables([Dungeon])

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
