from albibong.classes.event_handler.handle_event_character_equipment_changed import (
    handle_event_character_equipment_changed,
)
from albibong.classes.event_handler.handle_event_health import (
    handle_event_health_update,
    handle_event_health_updates,
)
from albibong.classes.event_handler.handle_event_in_combat_state_update import (
    handle_event_in_combat_state_update,
)
from albibong.classes.event_handler.handle_event_might_and_favor_received_event import (
    handle_event_might_and_favor_received_event,
)
from albibong.classes.event_handler.handle_event_new_character import (
    handle_event_new_character,
)
from albibong.classes.event_handler.handle_event_other_grabbed_loot import (
    handle_event_other_grabbed_loot,
)
from albibong.classes.event_handler.handle_event_party import (
    handle_event_party_disbanded,
    handle_event_party_joined,
    handle_event_party_player_joined,
    handle_event_party_player_left,
)
from albibong.classes.event_handler.handle_event_update_fame import (
    handle_event_update_fame,
)
from albibong.classes.event_handler.handle_event_update_re_spec_points import (
    handle_event_update_re_spec_points,
)
from albibong.classes.event_handler.handle_operation_change_cluster import (
    handle_operation_change_cluster,
)
from albibong.classes.event_handler.handle_operation_farmable_harvest import (
    handle_operation_farmable_get_product,
    handle_operation_farmable_harvest,
)
from albibong.classes.event_handler.radar_event_harvestable_object import (
    radar_event_new_harvestable_object,
    radar_event_new_simple_harvestable_object,
    radar_event_harvest_finished,
)
from albibong.classes.event_handler.radar_event_dungeon_object import (
    radar_event_random_dungeon_position_info,
    radar_event_new_random_dungeon_exists
)

from albibong.classes.event_handler.radar_event_chest_object import (
    radar_event_new_loot_chest,
    radar_event_new_treasure_chest,
    radar_event_new_match_loot_chest_object
)

from albibong.classes.event_handler.radar_event_leave import (
    radar_event_leave
)

from albibong.classes.event_handler.radar_event_mobs_object import (
    radar_event_new_mob,
    radar_event_mob_change_state
)


from albibong.classes.event_handler.handle_operation_join import handle_operation_join
from albibong.classes.event_handler.handle_operation_move import handle_operation_move
from albibong.classes.world_data import WorldData
from albibong.resources.EventCode import EventCode
from albibong.resources.OperationCode import OperationCode

EVENT_TYPE_PARAMETER = 252
REQUEST_TYPE_PARAMETER = 253
RESPONSE_TYPE_PARAMETER = 253


class EventHandler:
    def __init__(self):
        self.request_handler = {}
        self.response_handler = {}
        self.event_handler = {}

        # Event Handler
        self.event_handler[EventCode.NEW_CHARACTER.value] = handle_event_new_character
        self.event_handler[EventCode.HEALTH_UPDATE.value] = handle_event_health_update
        self.event_handler[EventCode.HEALTH_UPDATES.value] = handle_event_health_updates
        self.event_handler[EventCode.IN_COMBAT_STATE_UPDATE.value] = (
            handle_event_in_combat_state_update
        )

        self.event_handler[EventCode.UPDATE_FAME.value] = handle_event_update_fame
        self.event_handler[EventCode.UPDATE_RE_SPEC_POINTS.value] = (
            handle_event_update_re_spec_points
        )
        self.event_handler[EventCode.MIGHT_AND_FAVOR_RECEIVED_EVENT.value] = (
            handle_event_might_and_favor_received_event
        )

        self.event_handler[EventCode.OTHER_GRABBED_LOOT.value] = (
            handle_event_other_grabbed_loot
        )
        self.event_handler[EventCode.PARTY_JOINED.value] = handle_event_party_joined
        self.event_handler[EventCode.PARTY_DISBANDED.value] = (
            handle_event_party_disbanded
        )
        self.event_handler[EventCode.PARTY_PLAYER_JOINED.value] = (
            handle_event_party_player_joined
        )
        self.event_handler[EventCode.PARTY_PLAYER_LEFT.value] = (
            handle_event_party_player_left
        )
        self.event_handler[EventCode.CHARACTER_EQUIPMENT_CHANGED.value] = (
            handle_event_character_equipment_changed
        )

        # Radar Event Handler

        ## Resources
        self.event_handler[EventCode.NEW_HARVESTABLE_OBJECT.value] = (
            radar_event_new_harvestable_object
        )

        self.event_handler[EventCode.HARVESTABLE_CHANGE_STATE.value] = (
            radar_event_harvest_finished
        )

        self.event_handler[EventCode.NEW_SIMPLE_HARVESTABLE_OBJECT.value] = (
            radar_event_new_simple_harvestable_object
        )

        self.event_handler[EventCode.NEW_SIMPLE_HARVESTABLE_OBJECT_LIST.value] = (
            radar_event_new_simple_harvestable_object
        )

        ## Dungeons
        self.event_handler[EventCode.RANDOM_DUNGEON_POSITION_INFO.value] = (
            radar_event_random_dungeon_position_info
        )

        self.event_handler[EventCode.NEW_RANDOM_DUNGEON_EXIT.value] = (
            radar_event_new_random_dungeon_exists
        )


        ## chest
        self.event_handler[EventCode.NEW_LOOT_CHEST.value] = (
            radar_event_new_loot_chest
        )

        self.event_handler[EventCode.NEW_MATCH_LOOT_CHEST_OBJECT.value] = (
            radar_event_new_match_loot_chest_object
        )

        self.event_handler[EventCode.NEW_TREASURE_CHEST.value] = (
            radar_event_new_treasure_chest
        )

        ## Mobs
        self.event_handler[EventCode.NEW_MOB.value] = radar_event_new_mob
        self.event_handler[EventCode.MOB_CHANGE_STATE.value] = radar_event_mob_change_state
        

        ## Handle Action
        self.event_handler[EventCode.LEAVE.value] = radar_event_leave

        # Request Handler
        self.request_handler[OperationCode.MOVE.value] = handle_operation_move

        # Response Handler
        self.response_handler[OperationCode.JOIN.value] = handle_operation_join
        self.response_handler[OperationCode.CHANGE_CLUSTER.value] = (
            handle_operation_change_cluster
        )
        self.response_handler[OperationCode.FARMABLE_GET_PRODUCT.value] = (
            handle_operation_farmable_get_product
        )
        self.response_handler[OperationCode.FARMABLE_HARVEST.value] = (
            handle_operation_farmable_harvest
        )

    def on_request(self, world_data: WorldData, parameters):
        if REQUEST_TYPE_PARAMETER not in parameters:
            return None

        if parameters[REQUEST_TYPE_PARAMETER] not in self.request_handler:
            return None

        handler = self.request_handler[parameters[REQUEST_TYPE_PARAMETER]]
        return handler(world_data, parameters)

    def on_response(self, world_data: WorldData, parameters):
        if RESPONSE_TYPE_PARAMETER not in parameters:
            return None

        if parameters[RESPONSE_TYPE_PARAMETER] not in self.response_handler:
            return None

        handler = self.response_handler[parameters[RESPONSE_TYPE_PARAMETER]]
        return handler(world_data, parameters)

    def on_event(self, world_data: WorldData, parameters):
        handle_event = False
        call_type = None
        
        if EVENT_TYPE_PARAMETER in parameters:
            if parameters[EVENT_TYPE_PARAMETER] in self.event_handler:
                handle_event = True
                call_type = parameters[EVENT_TYPE_PARAMETER]
        else:
            if len(parameters) == 2 and 1 in parameters and parameters[1][0] == EventCode.MOVE.value:
                handle_event = True
                call_type = EventCode.MOVE.value

        if handle_event:
            if call_type == EventCode.MOVE.value:
                id = parameters[0]
                world_data.radar.handle_event_move(id, parameters)
            else:
                handler = self.event_handler[call_type]
                return handler(world_data, parameters)
