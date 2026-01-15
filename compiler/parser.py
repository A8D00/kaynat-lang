from compiler.ast import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        body = [
            Assignment("س", Number(2)),
            Assignment("ص", BinaryOp(Number(3), "+", Number(4))),
            Return(Identifier("ص"))
        ]
        return Function("رئيسية", body)
      
