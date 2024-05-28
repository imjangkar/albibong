from enum import Enum

class MessageType(Enum):
    OperationRequest = 2
    OperationResponse = 3
    Event = 4