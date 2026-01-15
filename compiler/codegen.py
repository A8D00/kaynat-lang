# compiler/codegen.py
# تحويل IR إلى Machine Code (0/1)

def generate_machine_code(ir_functions):
    """
    ir_functions: قائمة من IRFunction
    return: string ثنائي (0 و 1 فقط)
    """

    binary = ""

    for fn in ir_functions:
        for instr in fn.body:

            # دعم IRReturn فقط حاليًا
            if hasattr(instr, "opcode") and hasattr(instr, "value"):
                opcode = format(instr.opcode, "08b")  # 8 bits
                operand = instr.value                  # 8 bits (جاهز مسبقًا)
                binary += opcode + operand
            else:
                raise RuntimeError("تعليمة IR غير مدعومة")

    return binary
    
