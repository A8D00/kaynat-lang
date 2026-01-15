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
from compiler.lexer import tokenize
from compiler.parser import Parser
from compiler.ir import IRBuilder
from compiler.codegen import generate_machine_code

def main():
    if len(sys.argv) < 2:
        print("استخدم: python main.py <file.كيان>")
        return

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        source_code = f.read()

    tokens = tokenize(source_code)
    parser = Parser(tokens)
    ast = parser.parse()

    ir = IRBuilder().build(ast)
    machine_code = generate_machine_code(ir)

    print("Machine Code:")
    print(machine_code)

if __name__ == "__main__":
    main()
    
