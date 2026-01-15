import re

TOKEN_SPEC = [
    ("NUMBER", r"\d+"),
    ("ID", r"[أ-ي_]+"),
    ("PLUS", r"\+"),
    ("MINUS", r"-"),
    ("ASSIGN", r"="),
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("LBRACE", r"\{"),
    ("RBRACE", r"\}"),
    ("RETURN", r"ارجع"),
    ("WHILE", r"بينما"),
    ("IF", r"اذا"),
    ("SKIP", r"[ \t\n]+"),
]

def tokenize(code):
    tokens = []
    for name, pattern in TOKEN_SPEC:
        for match in re.finditer(pattern, code):
            tokens.append((name, match.group()))
    return tokens
  
