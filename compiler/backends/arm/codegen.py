from .isa import ARM_ISA

def generate_arm(ir):
    asm = []
    for instr in ir:
        if instr.opcode == "LOAD_CONST":
            asm.append(f"{ARM_ISA['LOAD_CONST']}{instr.operand}")
        else:
            asm.append(ARM_ISA.get(instr.opcode, ""))
    return "\n".join(asm)
  
