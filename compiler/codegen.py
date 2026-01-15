# compiler/codegen.py
# تحويل IR إلى Machine Code (0/1)

def generate_machine_code(ir_functions):
    binary = ""

    for fn in ir_functions:
        for instr in fn.body:

            if instr.__class__.__name__ == "IRLoadConst":
                binary += "00000001" + format(instr.value, "08b")

            elif instr.__class__.__name__ == "IRAdd":
                binary += "00000010" + "00000000"

            elif instr.__class__.__name__ == "IRSub":
                binary += "00000011" + "00000000"

            elif instr.__class__.__name__ == "IRReturn":
                binary += "11111111" + format(instr.value, "08b")

            else:
                raise RuntimeError("تعليمة IR غير مدعومة")

    return binary
