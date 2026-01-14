# compiler/parser.py

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

class Number(Node):
    def __init__(self, value):
        self.value = value
