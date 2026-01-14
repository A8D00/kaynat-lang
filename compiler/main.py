# compiler/main.py
# نقطة الدخول لمترجم لغة الكيانات

from lexer import tokenize
from parser import parse
from ir import IRBuilder
from codegen import CodeGenerator

def compile_source(source_code):
    tokens = tokenize(source_code)
    ast = parse(tokens)

    ir_builder = IRBuilder()
    ir = ir_builder.build(ast)

    codegen = CodeGenerator()
    asm = codegen.generate(ir)

    return asm


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("الاستخدام: kaynat <file.كيان>")
        sys.exit(1)

    filename = sys.argv[1]

    with open(filename, "r", encoding="utf-8") as f:
        source = f.read()

    assembly = compile_source(source)
    print(assembly)
