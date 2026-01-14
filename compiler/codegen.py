# compiler/codegen.py
# توليد Assembly x86-64 من IR لغة الكيانات

class CodeGenerator:
    def generate(self, ir_functions):
        asm = []

        # رأس البرنامج
        asm.append("section .text")
        asm.append("global _start")
        asm.append("")

        for fn in ir_functions:
            asm.extend(self.generate_function(fn))

        return "\n".join(asm)

    def generate_function(self, fn):
        code = []

        # نقطة الدخول (حالياً نعتبر رئيسية فقط)
        if fn.name == "رئيسية":
            code.append("_start:")

        for instr in fn.body:
            if instr.__class__.__name__ == "IRReturn":
                code.extend(self.generate_return(instr))

        return code

    def generate_return(self, instr):
        code = []

        # حاليًا: نحول القيمة إلى عدد صحيح (مرحلة أولى)
        value = int(instr.value)

        # mov rax, value
        code.append(f"    mov rax, {value}")

        # exit syscall
        code.append("    mov rdi, rax")   # status
        code.append("    mov rax, 60")    # sys_exit
        code.append("    syscall")

        return code
