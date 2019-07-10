from opcodes import *


globals().update(OPCODES.__members__)


def run(code):
    vm = VirtualMachine()

    i = 0 # index in code
    while True:
        op = code[i]
        if op == PUSH:
            i += 1
            vm.stack.append(code[i])
        elif op == ADD:
            b = vm.stack.pop()
            a = vm.stack.pop()
            vm.stack.append(a+b)
        elif op == SUB:
            b = vm.stack.pop()
            a = vm.stack.pop()
            vm.stack.append(a-b)
        elif op == AND:
            b = vm.stack.pop()
            a = vm.stack.pop()
            vm.stack.append(a & b)
        elif op == PRINT:
            print(vm.stack.pop(), end='')
        elif op == OUTCHAR:
            print(chr(vm.stack.pop()), end='')
        elif op == LT:
            b = vm.stack.pop()
            a = vm.stack.pop()
            vm.stack.append(int(a < b))
        elif op == JMP:
            i = code[i+1]-1
        elif op == JZ:
            i += 1
            addr = code[i]
            if vm.stack.pop() == 0:
                i = addr-1
        elif op == GSTORE:
            i += 1
            addr = code[i]
            vm.globals[addr] = vm.stack.pop()
        elif op == GLOAD:
            i += 1
            addr = code[i]
            vm.stack.append(vm.globals[addr])
        elif op == HALT:
            return
        else:
            raise Exception(f"Invalid opcode: {op}")
        i += 1


class VirtualMachine:
    def __init__(self):
        # Stack implemented as list
        # append() - add to stack
        # pop() - remove from stack
        self.stack = []

        # Globals implemented as dictionary
        # Keys will be addresses in memory (integer)
        self.globals = {}
