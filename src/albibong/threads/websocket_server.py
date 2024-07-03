import asyncio
from datetime import timedelta
import json
import os
import queue
import threading

import websockets

from albibong.classes.dungeon import Dungeon
from albibong.classes.logger import Logger

logger = Logger(__name__, stdout=True, log_to_file=False)
logger_file = Logger(__name__)

home_dir = os.path.expanduser("~")
FILENAME = f"{home_dir}/Albibong/list_dungeon.json"


class WebsocketServer(threading.Thread):
    def __init__(self, name, in_queue) -> None:
        super().__init__()
        self.name = name
        self.in_queue = in_queue
        self.stop_event = threading.Event()
        self.connections = set()

    async def handler(self, websocket):
        from albibong.classes.world_data import get_world_data

        self.connections.add(websocket)
        try:
            world_data = get_world_data()
            me = world_data.me
            # if me.id != None:
            event_init_world = {
                "type": "init_world",
                "payload": {
                    "me": {
                        "username": me.username,
                        "fame": me.fame_gained,
                        "re_spec": me.re_spec_gained,
                        "silver": me.silver_gained,
                    },
                    "world": {
                        "map": (
                            world_data.current_map.name
                            if world_data.current_map
                            else "not initialized"
                        ),
                        "dungeon": (
                            Dungeon.serialize(world_data.current_dungeon)
                            if world_data.current_dungeon
                            else None
                        ),
                        "isDPSMeterRunning": world_data.is_dps_meter_running,
                    },
                },
            }
            # logger.info(f"initializing character: {event}")
            await websocket.send(json.dumps(event_init_world))
            try:
                with open(FILENAME) as json_file:
                    list_dungeon = json.load(json_file)
                    event_init_dungeon_list = {
                        "type": "update_dungeon",
                        "payload": {"list_dungeon": list_dungeon},
                    }
            except:
                event_init_dungeon_list = {
                    "type": "update_dungeon",
                    "payload": {"list_dungeon": []},
                }
            await websocket.send(json.dumps(event_init_dungeon_list))

            async for message in websocket:
                event = json.loads(message)
                # print(event)
                if event["type"] == "update_is_dps_meter_running":
                    world_data.is_dps_meter_running = event["payload"]["value"]
                    reply = {
                        "type": "update_is_dps_meter_running",
                        "payload": {"value": world_data.is_dps_meter_running},
                    }
                    logger_file.log_dps_meter_state(world_data.is_dps_meter_running)
                    await websocket.send(json.dumps(reply))
                elif event["type"] == "reset_dps_meter":
                    party_members = event["payload"]["party_members"]
                    for member in party_members:
                        char = world_data.characters[member]
                        char.damage_dealt = 0
                        char.healing_dealt = 0
                        char.total_combat_duration = timedelta(0, 0)
                    reply = {
                        "type": "update_dps",
                        "payload": {
                            "party_members": world_data.serialize_party_members()
                        },
                    }
                    await websocket.send(json.dumps(reply))
                elif event["type"] == "refresh_dungeon_list":
                    try:
                        with open(FILENAME) as json_file:
                            list_dungeon = json.load(json_file)
                            reply = {
                                "type": "update_dungeon",
                                "payload": {"list_dungeon": list_dungeon},
                            }
                    except:
                        reply = {
                            "type": "update_dungeon",
                            "payload": {"list_dungeon": []},
                        }
                    await websocket.send(json.dumps(reply))
                elif event["type"] == "update_dungeon_data":
                    updated_tier = event["payload"]["list_dungeon"]
                    with open(FILENAME, "w") as json_file:
                        json.dump(updated_tier, json_file)

                    reply = {
                        "type": "update_dungeon",
                        "payload": {"list_dungeon": updated_tier},
                    }
                    await websocket.send(json.dumps(reply))

            event = {}
            send_event(event)
        finally:
            self.connections.remove(websocket)

    async def main(self):
        async with websockets.serve(self.handler, "", 8081):
            while True:
                if self.stop_event.is_set():
                    return

                while not self.in_queue.empty():
                    if self.stop_event.is_set():
                        return

                    event = self.in_queue.get()
                    if len(self.connections) > 0:
                        # logger.info(f"broadcast {event}")
                        websockets.broadcast(self.connections, json.dumps(event))
                        await asyncio.sleep(0)

                await asyncio.sleep(0)

    def run(self):
        logger.info(f"Thread {self.name} started")

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.main())

    def stop(self):
        logger.info(f"Thread {self.name} stopped")
        self.stop_event.set()


event_queue = queue.Queue()
ws_server = WebsocketServer(name="ws_server", in_queue=event_queue)


def send_event(event):
    event_queue.put(event)


def get_ws_server():
    return ws_server
