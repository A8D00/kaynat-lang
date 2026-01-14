# target x86_64 Linux

def generate_exit(value: int) -> str:
    return f"""
section .text
global _start

_start:
    mov rax, 60
    mov rdi, {value}
    syscall
"""
