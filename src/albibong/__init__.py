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
from peewee_migrate import Router
from scapy.all import rdpcap

from albibong.classes.logger import Logger
from albibong.classes.packet_handler import PacketHandler
from albibong.classes.utils import Utils
from albibong.models.models import SQLITE_DB, db
from albibong.threads.http_server import HttpServerThread
from albibong.threads.packet_handler_thread import PacketHandlerThread
from albibong.threads.sniffer_thread import SnifferThread
from albibong.threads.websocket_server import get_ws_server

logger = Logger(__name__, stdout=True, log_to_file=False)
PORT = random.randrange(8500, 8999)

home_dir = os.path.expanduser("~")
DUNGEON_JSON = f"{home_dir}/Albibong/list_dungeon.json"

current_path = os.path.dirname(__file__)
MIGRATION_FOLDER = os.path.join(current_path, f"migrations")


def read_pcap(path):
    packet_handler = PacketHandler()
    scapy_cap = rdpcap(path)
    for packet in scapy_cap:
        packet_handler.handle(packet)


def get_dungeon_end_time(str, start_time):
    timer = str.split(":")
    seconds = int(timer[0]) * 3600 + int(timer[1]) * 60 + int(timer[2])
    return timedelta(seconds=seconds) + start_time


def check_db_validity():
    migrate = Router(db, migrate_dir=MIGRATION_FOLDER)

    if Path(SQLITE_DB).is_file() == False:
        if Path(DUNGEON_JSON).is_file() == True:

            migrate.run("001_init")

            # convert json db to sqlite db
            json_data = json.load(open(DUNGEON_JSON))

            for dungeon in json_data:
                start_time = datetime.strptime(
                    dungeon["date_time"], "%a %d %b %Y, %I:%M%p"
                )
                type_splitted = set(dungeon["type"].split("_"))

                if "CORRUPTED" in type_splitted:
                    converted_type = "CORRUPTED DUNGEON"
                elif "HARDCORE" in type_splitted:
                    converted_type = "HARDCORE EXPEDITION"
                elif "10V10" in type_splitted:
                    converted_type = "HELLGATE 10V10"
                elif "5V5" in type_splitted:
                    converted_type = "HELLGATE 5V5"
                elif "2V2" in type_splitted:
                    converted_type = "HELLGATE 2V2"
                elif "DUNGEON" in type_splitted:
                    converted_type = "STATIC DUNGEON"
                elif "RANDOMDUNGEON" in type_splitted:
                    converted_type = "SPAWN DUNGEON"

                asd = [
                    ("id", str(uuid.uuid4())),
                    ("type", f"{converted_type}"),
                    ("name", f'{dungeon["name"]}'),
                    ("tier", f'{dungeon["tier"]}'),
                    ("fame", f'{dungeon["fame"]}'),
                    ("silver", f'{dungeon["silver"]}'),
                    ("re_spec", f'{dungeon["re_spec"]}'),
                    ("start_time", f"{start_time}"),
                    (
                        "end_time",
                        f'{get_dungeon_end_time(dungeon["time_elapsed"], start_time)}',
                    ),
                    ("meter", ""),
                ]

                columns = ", ".join([x[0] for x in asd])
                values = ", ".join([f'"{x[1]}"' for x in asd])
                sql_query = f"INSERT INTO dungeon ({columns}) VALUES ({values})"

                db.execute_sql(sql_query)

    migrate.run()


def sniff(useWebview, is_debug=False):

    check_db_validity()

    _sentinel = object()
    packet_queue = queue.Queue()

    p = SnifferThread(
        name="sniffer", out_queue=packet_queue, sentinel=_sentinel, is_debug=is_debug
    )
    c = PacketHandlerThread(
        name="packet_handler",
        in_queue=packet_queue,
        sentinel=_sentinel,
    )

    p.start()
    c.start()

    ws_server = get_ws_server()
    ws_server.start()

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
        if sys.argv[-1] == "--debug":
            Utils.get_user_specifications("pip")
            sniff(useWebview, is_debug=True)
        else:
            ws_server = get_ws_server()
            ws_server.start()
            read_pcap(sys.argv[1])
    else:
        sniff(useWebview)
