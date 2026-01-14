# compiler/linker.py
import subprocess
import os

def link(obj_file: str, output: str = "a.out"):
    subprocess.run(["ld", obj_file, "-o", output], check=True)
    return output
