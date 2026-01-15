from compiler.isa import ISA

def run(binary):
    pc = 0
    stack = []
    mem = {}

    while pc < len(binary):
        opcode = int(binary[pc:pc+8], 2)
        operand = int(binary[pc+8:pc+16], 2)
        pc += 16

        if opcode == ISA["LOAD_CONST"]:
            stack.append(operand)
        elif opcode == ISA["LOAD_VAR"]:
            stack.append(mem.get(operand, 0))
        elif opcode == ISA["STORE"]:
            mem[operand] = stack.pop()
        elif opcode == ISA["ADD"]:
            b = stack.pop(); a = stack.pop()
            stack.append(a + b)
        elif opcode == ISA["RETURN"]:
            return stack.pop()
