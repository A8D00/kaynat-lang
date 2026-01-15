from compiler.isa import ISA

def generate_vm_code(ir):
    binary = ""
    for instr in ir:
        opcode = ISA[instr.opcode]
        operand = instr.operand if instr.operand is not None else 0
        binary += f"{opcode:08b}{operand:08b}"
    return binary
  
