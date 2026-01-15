def generate_machine_code(ir_functions):
    bits = ""
    for fn in ir_functions:
        for instr in fn.body:
            bits += format(instr.opcode, "08b") + instr.operand
    return bits
  
