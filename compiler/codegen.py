# compiler/codegen.py
# تحويل IR إلى Machine Code (0/1)

def generate_machine_code(ir_functions):
    """
    ir_functions: قائمة IRFunction
    return: string من 0 و 1 فقط
    """
    binary = ""

    for fn in ir_functions:
        for instr in fn.body:
            if instr.__class__.__name__ == "IRReturn":
                opcode = format(instr.opcode, "08b")
                value = instr.value  # أصلاً ثنائي
                binary += opcode + value

    return binary
