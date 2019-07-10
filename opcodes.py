from enum import Enum, auto


class OPCODES(Enum):
    PUSH = auto()
    SUB = auto()
    ADD = auto()
    AND = auto()
    PRINT = auto()
    OUTCHAR = auto()
    GSTORE = auto()
    GLOAD = auto()
    LT = auto()
    JMP = auto()
    JZ = auto()
    HALT = auto()
