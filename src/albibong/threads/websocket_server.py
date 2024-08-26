import asyncio
import json
import queue
import threading
from datetime import datetime, timedelta

import websockets

from albibong.classes.dungeon import Dungeon
from albibong.classes.location import Island
from albibong.classes.logger import Logger

logger = Logger(__name__, stdout=True, log_to_file=False)
logger_file = Logger(__name__)


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
            event_init_world = {
                "type": "init_world",
                "payload": {
                    "me": {
                        "username": me.username,
                        "fame": me.fame_gained,
                        "re_spec": me.re_spec_gained,
                        "silver": me.silver_gained,
                        "might": me.might_gained,
                        "favor": me.favor_gained,
                    },
                    "world": {
                        "map": (
                            world_data.current_map.name
                            if world_data.current_map
                            else "zone in to other map to initialize"
                        ),
                        "dungeon": (
                            world_data.current_dungeon.name
                            if world_data.current_dungeon
                            else "zone in to other map to initialize"
                        ),
                        "isDPSMeterRunning": world_data.is_dps_meter_running,
                    },
                },
            }
            await websocket.send(json.dumps(event_init_world))
            event_init_dungeon_list = {
                "type": "update_dungeon",
                "payload": {"list_dungeon": Dungeon.get_all_dungeon()},
            }
            await websocket.send(json.dumps(event_init_dungeon_list))
            event_init_island_list = {
                "type": "update_island",
                "payload": {"list_island": Island.get_all_island()},
            }
            await websocket.send(json.dumps(event_init_island_list))
            total_harvest_reply = {
                "type": "update_total_harvest_by_date",
                "payload": Island.get_total_harvest_by_date(),
            }
            await websocket.send(json.dumps(total_harvest_reply))
            async for message in websocket:
                event = json.loads(message)
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
                        "type": "update_damage_meter",
                        "payload": {
                            "party_members": world_data.serialize_party_members()
                        },
                    }
                    await websocket.send(json.dumps(reply))
                elif event["type"] == "reset_player_stats":
                    world_data.me.fame_gained = 0
                    world_data.me.re_spec_gained = 0
                    world_data.me.silver_gained = 0
                    world_data.me.might_gained = 0
                    world_data.me.favor_gained = 0

                    fame = {
                        "type": "update_fame",
                        "payload": {
                            "username": world_data.me.username,
                            "fame_gained": world_data.me.fame_gained,
                        },
                    }
                    re_spec = {
                        "type": "update_re_spec",
                        "payload": {
                            "username": world_data.me.username,
                            "re_spec_gained": world_data.me.re_spec_gained,
                        },
                    }
                    silver = {
                        "type": "update_silver",
                        "payload": {
                            "username": world_data.me.username,
                            "silver_gained": world_data.me.silver_gained,
                        },
                    }
                    might_and_favor = {
                        "type": "update_might_and_favor",
                        "payload": {
                            "username": world_data.me.username,
                            "favor_gained": world_data.me.favor_gained,
                            "might_gained": world_data.me.might_gained,
                        },
                    }
                    await websocket.send(json.dumps(fame))
                    await websocket.send(json.dumps(re_spec))
                    await websocket.send(json.dumps(silver))
                    await websocket.send(json.dumps(might_and_favor))

                elif event["type"] == "refresh_dungeon_list":
                    reply = {
                        "type": "update_dungeon",
                        "payload": {"list_dungeon": Dungeon.get_all_dungeon()},
                    }
                    await websocket.send(json.dumps(reply))
                elif event["type"] == "update_dungeon_tier":
                    id = event["payload"]["id"]
                    value = event["payload"]["value"]
                    dungeon: Dungeon = Dungeon.update(tier=value).where(
                        Dungeon.id == id
                    )
                    dungeon.execute()
                    reply = {
                        "type": "update_dungeon",
                        "payload": {"list_dungeon": Dungeon.get_all_dungeon()},
                    }
                    await websocket.send(json.dumps(reply))
                elif event["type"] == "update_dungeon_name":
                    id = event["payload"]["id"]
                    value = event["payload"]["value"]
                    dungeon: Dungeon = Dungeon.update(name=value).where(
                        Dungeon.id == id
                    )
                    dungeon.execute()
                    reply = {
                        "type": "update_dungeon",
                        "payload": {"list_dungeon": Dungeon.get_all_dungeon()},
                    }
                    await websocket.send(json.dumps(reply))
                elif event["type"] == "refresh_island_list":
                    refresh_island_reply = {
                        "type": "update_island",
                        "payload": {"list_island": Island.get_all_island()},
                    }
                    total_harvest_reply = {
                        "type": "update_total_harvest_by_date",
                        "payload": Island.get_total_harvest_by_date(),
                    }
                    await websocket.send(json.dumps(refresh_island_reply))
                    await websocket.send(json.dumps(total_harvest_reply))
                elif event["type"] == "update_total_harvested_date_range":
                    date = event["payload"]["date"]
                    format = "%Y-%m-%d"
                    total_harvest_reply = {
                        "type": "update_total_harvest_by_date",
                        "payload": Island.get_total_harvest_by_date(
                            date=datetime.strptime(date, format)
                        ),
                    }
                    await websocket.send(json.dumps(total_harvest_reply))

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
