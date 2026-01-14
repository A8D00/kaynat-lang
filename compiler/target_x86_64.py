# compiler/target_x86_64.py

def generate_return(value: int) -> str:
    return f"""
section .text
global _start

_start:
    mov rax, 60
    mov rdi, {value}
    syscall
"""
