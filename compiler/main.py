# compiler/main.py
# نقطة الدخول لمترجم لغة الكيانات

from compiler.codegen import generate_machine_code

from lexer import tokenize
from parser import parse
from ir import IRBuilder
from codegen import CodeGenerator

from assembler import assemble
from linker import link
from target import get_target

import sys

def compile_source(source_code):
    tokens = tokenize(source_code)
    ast = parse(tokens)

    ir_builder = IRBuilder()
    ir = ir_builder.build(ast)

machine_code = generate_machine_code(ir)

print("=== Machine Code (0/1 فقط) ===")
print(machine_code)
    
    codegen = CodeGenerator()
    generate_exit = get_target()
asm = generate_exit(5)

    return asm

    if len(sys.argv) < 2:
        print("الاستخدام: kaynat <file.كيان>")
        sys.exit(1)

    filename = sys.argv[1]

    with open(filename, "r", encoding="utf-8") as f:
        source = f.read()

    # توليد Assembly حقيقي
asm = generate_return(5)

# تحويل Assembly إلى Object file
obj = assemble(asm)

# ربطه لإنتاج ملف تنفيذي (0 و 1)
binary = link(obj)

print("تم إنشاء ملف تنفيذي:", binary)
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("يرجى تمرير ملف .كيان")
        sys.exit(1)

    source_file = sys.argv[1]
    compile_file(source_file)
    from compiler.vm import VirtualMachine

# بعد توليد binary_code
vm = VirtualMachine(binary_code)
result = vm.run()

print("ناتج التنفيذ:", result)
    
