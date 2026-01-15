import re

TOKEN_SPEC = [
    ("NUMBER",   r"\d+"),          # أعداد صحيحة
    ("ID",       r"[أ-ي_]+"),       # معرفات عربية
    ("PLUS",     r"\+"),            # +
    ("MINUS",    r"-"),             # -
    ("ASSIGN",   r"="),             # =
    ("LPAREN",   r"\("),
    ("RPAREN",   r"\)"),
    ("NEWLINE",  r"\n"),
    ("SKIP",     r"[ \t]+"),
]

def tokenize(code):
    tokens = []
    for name, pattern in TOKEN_SPEC:
        for match in re.finditer(pattern, code):
            tokens.append((name, match.group()))
    return tokens
  
