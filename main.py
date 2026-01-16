from frontend.lexer import tokenize
from frontend.parser import parse
from semantic.analyzer import analyze
from ir.ir_builder import build_ir
from exec.ks_vm import KSVM

def main():
    source = """
    كيان عداد:
        الحالة = 0
        قرار:
            الحالة = الحالة + 1
    """

    tokens = tokenize(source)
    ast = parse(tokens)
    analyze(ast)
    ir = build_ir(ast)

    vm = KSVM(ir)
    vm.run()

if __name__ == "__main__":
    main()
