# compiler/vm.py
# آلة افتراضية للغة الكيانات

class VirtualMachine:
    def __init__(self, binary_code):
        self.code = binary_code
        self.pc = 0          # Program Counter
        self.stack = []      # Stack بسيط

    def fetch(self):
        """جلب تعليمة واحدة (16 بت)"""
        instr = self.code[self.pc:self.pc + 16]
        self.pc += 16
        return instr

    def decode_execute(self, instr):
    opcode = instr[:8]
    operand = instr[8:]

    if opcode == "00000001":  # LOAD_CONST
        value = int(operand, 2)
        self.stack.append(value)

    elif opcode == "00000010":  # ADD
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a + b)

    elif opcode == "00000011":  # SUB
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a - b)

    elif opcode == "11111111":  # RETURN
        value = int(operand, 2)
        return value

    else:
        raise RuntimeError(f"Opcode غير معروف: {opcode}")

        if opcode == "11111111":  # RETURN
            value = int(operand, 2)
            self.stack.append(value)
            return "HALT"

        else:
            raise RuntimeError(f"Opcode غير معروف: {opcode}")

    def run(self):
        while self.pc < len(self.code):
            instr = self.fetch()
            result = self.decode_execute(instr)
            if result == "HALT":
                break

        return self.stack[-1] if self.stack else None
