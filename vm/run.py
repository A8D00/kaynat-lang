from compiler.isa import ISA
from runtime.memory import Memory

class VM:
    def __init__(self, code):
        self.code = code
        self.pc = 0
        self.stack = []
        self.memory = Memory()

    def run(self):
        while self.pc < len(self.code):
            opcode = int(self.code[self.pc:self.pc+8], 2)
            operand = int(self.code[self.pc+8:self.pc+16], 2)
            self.pc += 16

            if opcode == ISA["LOAD_CONST"]:
                self.stack.append(operand)
            elif opcode == ISA["ADD"]:
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a + b)
            elif opcode == ISA["RETURN"]:
                return self.stack.pop()
              
