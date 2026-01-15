def run(binary):
    pc = 0
    stack = []

    while pc < len(binary):
        opcode = int(binary[pc:pc+8], 2)
        operand = int(binary[pc+8:pc+16], 2)
        pc += 16

        if opcode == 0b00000001:  # LOAD_CONST
            stack.append(operand)

        elif opcode == 0b00000100:  # ADD
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)

        elif opcode == 0b11111111:  # RETURN
            return operand
