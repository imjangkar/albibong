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

        # Request Handler
        self.request_handler[OperationCode.MOVE.value] = handle_operation_move

        # Response Handler
        self.response_handler[OperationCode.JOIN.value] = handle_operation_join
        self.response_handler[OperationCode.CHANGE_CLUSTER.value] = (
            handle_operation_change_cluster
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
        if EVENT_TYPE_PARAMETER not in parameters:
            return None

        if parameters[EVENT_TYPE_PARAMETER] not in self.event_handler:
            return None

        handler = self.event_handler[parameters[EVENT_TYPE_PARAMETER]]
        return handler(world_data, parameters)
