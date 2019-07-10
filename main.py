from opcodes import *
from vm import run


globals().update(OPCODES.__members__)


POWER_OF_TWO = [
    PUSH, 64,
    PUSH, 64,
    PUSH, 1,
    SUB,
    AND,
    PRINT,

    HALT,
]

HELLO_WORLD = [
    PUSH, 10, PUSH, 33, PUSH, 100,
    PUSH, 108, PUSH, 114, PUSH, 111,
    PUSH, 87, PUSH, 32, PUSH, 44,
    PUSH, 111, PUSH, 108, PUSH, 108,
    PUSH, 101, PUSH, 72,

    OUTCHAR, OUTCHAR, OUTCHAR,
    OUTCHAR, OUTCHAR, OUTCHAR,
    OUTCHAR, OUTCHAR, OUTCHAR,
    OUTCHAR, OUTCHAR, OUTCHAR,
    OUTCHAR, OUTCHAR,

    HALT,
]

# for x=0; x<15; x++
LOOP = [
    # Store 15
    PUSH, 15,
    GSTORE, 0,

    # Store x=0
    PUSH, 0,
    GSTORE, 1,

    # Check condition x < y
    GLOAD, 1,
    GLOAD, 0,
    LT,
    JZ, 30,

    # Print x
    GLOAD, 1,
    PRINT,
    PUSH, 32,
    OUTCHAR,

    # Increment x
    GLOAD, 1,
    PUSH, 1,
    ADD,
    GSTORE, 1,

    # Jump to start of loop
    JMP, 8,

    HALT,
]

if __name__ == '__main__':
    run(POWER_OF_TWO)
    print()
    run(HELLO_WORLD)
    print()
    run(LOOP)
