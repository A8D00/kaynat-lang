from compiler.ir.ir import IRInstruction

def build_ir(ast):
    ir = []
    node = ast.body

    ir.append(IRInstruction("LOAD_CONST", node.left.value))
    ir.append(IRInstruction("LOAD_CONST", node.right.value))

    if node.op == "PLUS":
        ir.append(IRInstruction("ADD"))

    ir.append(IRInstruction("RETURN"))
    return ir
  
