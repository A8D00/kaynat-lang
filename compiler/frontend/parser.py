from compiler.frontend.ast import NumberNode, BinaryOpNode, ProgramNode

def parse(tokens):
    # مثال مبسط: NUMBER + NUMBER
    left = NumberNode(int(tokens[0][1]))
    op = tokens[1][0]
    right = NumberNode(int(tokens[2][1]))
    return ProgramNode(BinaryOpNode(left, op, right))
  
