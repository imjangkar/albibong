from albibong.classes.event_handler.handle_operation_change_cluster import (
    handle_operation_change_cluster,
)
from albibong.classes.event_handler.handle_operation_join import handle_operation_join
from albibong.classes.event_handler.handle_operation_move import handle_operation_move
from albibong.classes.world_data import WorldData
from albibong.resources.OperationCode import OperationCode

EVENT_TYPE_PARAMETER = 252
REQUEST_TYPE_PARAMETER = 253
RESPONSE_TYPE_PARAMETER = 253


class EventHandler:
    def __init__(self):
        self.request_handler = {}
        self.response_handler = {}
        self.event_handler = {}

        self.request_handler[OperationCode.MOVE.value] = handle_operation_move

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
