# compiler/lexer.py
import sys
import re

# -------- تعريف أنواع الـ Tokens --------
TOKEN_SPEC = [
    ("KEYWORD",   r"\b(دالة|أرجع|عدد|اطبع)\b"),
    ("NUMBER",    r"\d+(?:,\d+)?"),
    ("IDENT",     r"[ء-ي_][ء-ي0-9_]*"),
    ("LPAREN",    r"\("),
    ("RPAREN",    r"\)"),
    ("LBRACE",    r"\{"),
    ("RBRACE",    r"\}"),
    ("NEWLINE",   r"\n"),
    ("SKIP",      r"[ \t]+"),
    ("MISMATCH",  r"."),
]

MASTER_REGEX = "|".join(
    f"(?P<{name}>{pattern})" for name, pattern in TOKEN_SPEC
)

# -------- قراءة الملف --------
if len(sys.argv) < 2:
    print("خطأ: لم يتم تمرير ملف")
    sys.exit(1)

path = sys.argv[1]

with open(path, "r", encoding="utf-8") as f:
    code = f.read()

# -------- التحليل --------
tokens = []

for match in re.finditer(MASTER_REGEX, code):
    kind = match.lastgroup
    value = match.group()

    if kind in ("SKIP", "NEWLINE"):
        continue
    elif kind == "MISMATCH":
        print(f"رمز غير معروف: {value}")
        sys.exit(1)
    else:
        tokens.append((kind, value))

# -------- الطباعة --------
for t in tokens:
    print(t)
