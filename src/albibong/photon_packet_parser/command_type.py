from enum import Enum

class CommandType(Enum):
    Disconnect = 4
    SendReliable = 6
    SendUnreliable = 7
    SendFragment = 8