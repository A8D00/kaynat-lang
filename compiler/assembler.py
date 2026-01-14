# compiler/assembler.py
import subprocess
import tempfile
import os

def assemble(asm_code: str) -> str:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".asm") as f:
        f.write(asm_code.encode("utf-8"))
        asm_file = f.name

    obj_file = asm_file.replace(".asm", ".o")

    subprocess.run(["nasm", "-felf64", asm_file, "-o", obj_file], check=True)

    return obj_file
