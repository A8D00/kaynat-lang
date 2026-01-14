class CodeGen:
    def generate(self, ir_functions):
        asm = []
        asm.append("section .text")
        asm.append("global _start")

        for fn in ir_functions:
            asm.extend(self.gen_function(fn))

        return "\n".join(asm)

    def gen_function(self, fn):
        code = []
        code.append("_start:")
        ret = fn.body[0].value

        # تحويل الرقم إلى int مؤقتًا
        code.append(f"    mov rax, {int(ret)}")
        code.append("    mov rdi, rax")
        code.append("    mov rax, 60")  # sys_exit
        code.append("    syscall")
        return code
