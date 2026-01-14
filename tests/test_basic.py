# اختبار أساسي للمترجم

from compiler.main import compile_source

def test_return_constant():
    source = """
دالة البداية() {
    ارجع 7
}
"""
    asm = compile_source(source)
    assert "7" in asm
