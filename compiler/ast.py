class Node:
    pass


class Program(Node):
    def __init__(self, functions):
        self.functions = functions


class Function(Node):
    def __init__(self, name, body):
        self.name = name
        self.body = body


class Return(Node):
    def __init__(self, value):
        self.value = value


class VarDecl(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Number(Node):
    def __init__(self, value):
        self.value = value


class Identifier(Node):
    def __init__(self, name):
        self.name = name


class BinaryOp(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
