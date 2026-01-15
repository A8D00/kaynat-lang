from compiler.frontend.lexer import tokenize
from compiler.frontend.parser import parse
from compiler.ir.builder import build_ir
from compiler.optimizer import optimize
from compiler.backends.vm.codegen import generate_vm_code

import sys

source = open(sys.argv[1], encoding="utf-8").read()

tokens = tokenize(source)
ast = parse(tokens)
ir = build_ir(ast)
ir = optimize(ir)

binary = generate_vm_code(ir)

with open("output.bin", "w") as f:
    f.write(binary)

print("✔ تم إنشاء output.bin")
