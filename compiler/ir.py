from compiler.isa import ISA

class IRInstruction: pass

class IRLoadConst(IRInstruction):
    def __init__(self, value):
        self.opcode = ISA["LOAD_CONST"]
        self.operand = format(value, "08b")

class IRLoadVar(IRInstruction):
    def __init__(self, addr):
        self.opcode = ISA["LOAD_VAR"]
        self.operand = format(addr, "08b")

class IRStore(IRInstruction):
    def __init__(self, addr):
        self.opcode = ISA["STORE"]
        self.operand = format(addr, "08b")

class IRAdd(IRInstruction):
    def __init__(self):
        self.opcode = ISA["ADD"]
        self.operand = "00000000"

class IRReturn(IRInstruction):
    def __init__(self):
        self.opcode = ISA["RETURN"]
        self.operand = "00000000"

class IRFunction:
    def __init__(self, name):
        self.name = name
        self.body = []

class IRBuilder:
    def __init__(self):
        self.vars = {}
        self.addr = 0

    def get_addr(self, name):
        if name not in self.vars:
            self.vars[name] = self.addr
            self.addr += 1
        return self.vars[name]

    def build_expr(self, expr, ir):
        from compiler.ast import Number, Identifier, BinaryOp
        if isinstance(expr, Number):
            ir.body.append(IRLoadConst(expr.value))
        elif isinstance(expr, Identifier):
            ir.body.append(IRLoadVar(self.get_addr(expr.name)))
        elif isinstance(expr, BinaryOp):
            self.build_expr(expr.left, ir)
            self.build_expr(expr.right, ir)
            ir.body.append(IRAdd())

    def build(self, ast):
        ir = IRFunction(ast.name)
        from compiler.ast import Assignment, Return
        for stmt in ast.body:
            if isinstance(stmt, Assignment):
                self.build_expr(stmt.value, ir)
                ir.body.append(IRStore(self.get_addr(stmt.name)))
            elif isinstance(stmt, Return):
                self.build_expr(stmt.value, ir)
                ir.body.append(IRReturn())
        return [ir]
      
