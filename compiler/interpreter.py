class Interpreter:
    def visit(self, node):
        method = "visit_" + node.__class__.__name__
        return getattr(self, method)(node)

    def visit_Program(self, node):
        for fn in node.functions:
            if fn.name == "رئيسية":
                return self.visit(fn)

    def visit_Function(self, node):
        return self.visit(node.body)

    def visit_Return(self, node):
        return self.visit(node.value)

    def visit_Number(self, node):
        return node.value
