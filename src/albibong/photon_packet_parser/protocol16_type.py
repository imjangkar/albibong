from enum import Enum

class Protocol16Type(Enum):
    UNKNOWN = 0
    NULL = 42
    DICTIONARY = 68
    STRINGARRAY = 97
    BYTE = 98
    DOUBLE = 100
    EVENTDATA = 101
    FLOAT = 102
    INTEGER = 105
    HASHTABLE = 104
    SHORT = 107
    LONG = 108
    INTEGERARRAY = 110
    BOOLEAN = 111
    OPERATIONRESPONSE = 112
    OPERATIONREQUEST = 113 
    STRING = 115
    BYTEARRAY = 120
    ARRAY = 121
    OBJECTARRAY = 122