# compiler/codegen.py
# تحويل IR إلى Machine Code (0/1)

def generate_machine_code(ir_functions):
    """
    ir_functions: قائمة IRFunction
    return: string من 0 و 1
    """
    binary = ""

    for fn in ir_functions:
        for instr in fn.body:
            opcode_bits = format(instr.opcode, "08b")
            binary += opcode_bits + instr.operand

    return binary
    
