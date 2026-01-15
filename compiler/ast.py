class Number:
    def __init__(self, value):
        self.value = value

class Identifier:
    def __init__(self, name):
        self.name = name

class BinaryOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Assignment:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Return:
    def __init__(self, value):
        self.value = value

class Function:
    def __init__(self, name, body):
        self.name = name
        self.body = body
      
