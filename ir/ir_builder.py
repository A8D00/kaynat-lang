from ir.ir_nodes import IREntity

def build_ir(ast):
    return IREntity(
        name=ast.name,
        state=ast.state,
        target=ast.decision.target,
        increment=ast.decision.increment
    )
