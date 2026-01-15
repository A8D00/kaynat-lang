import sys
from compiler.lexer import tokenize
from compiler.parser import Parser
from compiler.ir import IRBuilder
from compiler.codegen import generate_machine_code

def main():
    with open(sys.argv[1], encoding="utf-8") as f:
        src = f.read()

    tokens = tokenize(src)
    ast = Parser(tokens).parse()
    ir = IRBuilder().build(ast)
    binary = generate_machine_code(ir)

    with open("output.bin", "w") as f:
        f.write(binary)

    print("Machine Code:", binary)

if __name__ == "__main__":
    main()
  
