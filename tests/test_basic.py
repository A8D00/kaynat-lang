import unittest
import os
import sys

# السماح بالاستيراد من مجلد المشروع
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from compiler.lexer import tokenize
from compiler.parser import Parser
from compiler.ir import IRBuilder
from compiler.codegen import generate_machine_code
from vm.run import run


class TestKaynatLanguage(unittest.TestCase):

    def compile_and_run(self, source_code: str):
        # Lexer
        tokens = tokenize(source_code)

        # Parser → AST
        ast = Parser(tokens).parse()

        # AST → IR
        ir = IRBuilder().build(ast)

        # IR → Machine Code (0/1)
        binary = generate_machine_code(ir)

        # Run on VM
        result = run(binary)
        return result

    def test_simple_return(self):
        code = """
        س = 2
        ص = 3 + 4
        ارجع ص
        """
        result = self.compile_and_run(code)
        self.assertEqual(result, 7)

    def test_addition(self):
        code = """
        أ = 5
        ب = 6
        ج = أ + ب
        ارجع ج
        """
        result = self.compile_and_run(code)
        self.assertEqual(result, 11)

    def test_constant_only(self):
        code = """
        ارجع 9
        """
        result = self.compile_and_run(code)
        self.assertEqual(result, 9)


if __name__ == "__main__":
    unittest.main()
  
