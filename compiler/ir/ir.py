class IRInstruction:
    def __init__(self, opcode, operand=None):
        self.opcode = opcode
        self.operand = operand

    def __repr__(self):
        return f"{self.opcode} {self.operand if self.operand is not None else ''}"
      
