# compiler/lexer.py
import sys
import re

TOKEN_SPEC = [
    ("KEYWORD",   r"\b(دالة|أرجع|عدد|اطبع)\b"),
    ("NUMBER",    r"\d+(?:,\d+)?"),
    ("IDENT",     r"[ء-ي_][ء-ي0-9_]*"),
    ("LPAREN",    r"\("),
    ("RPAREN",    r"\)"),
    ("LBRACE",    r"\{"),
    ("RBRACE",    r"\}"),
    ("SKIP",      r"[ \t\n]+"),
    ("MISMATCH",  r"."),
]

MASTER_REGEX = "|".join(
    f"(?P<{name}>{pattern})" for name, pattern in TOKEN_SPEC
)

if len(sys.argv) < 2:
    print("خطأ: لم يتم تمرير ملف")
    sys.exit(1)

path = sys.argv[1]

with open(path, "r", encoding="utf-8") as f:
    code = f.read()

tokens = []

for match in re.finditer(MASTER_REGEX, code):
    kind = match.lastgroup
    value = match.group()

    if kind == "SKIP":
        continue
    elif kind == "MISMATCH":
        raise RuntimeError(f"رمز غير معروف: {value}")
    else:
        tokens.append((kind, value))

for t in tokens:
    print(t)

print("تم التحليل بنجاح")
