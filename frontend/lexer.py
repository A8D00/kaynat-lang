import re

TOKEN_SPEC = [
    ("ENTITY", r"كيان"),
    ("DECISION", r"قرار"),
    ("IDENT", r"[ء-يA-Za-z_]+"),
    ("NUMBER", r"\d+"),
    ("EQUAL", r"="),
    ("PLUS", r"\+"),
    ("COLON", r":"),
    ("NEWLINE", r"\n"),
    ("SKIP", r"[ \t]+"),
]

def tokenize(code):
    pos = 0
    tokens = []
    while pos < len(code):
        for kind, regex in TOKEN_SPEC:
            match = re.match(regex, code[pos:])
            if match:
                if kind != "SKIP" and kind != "NEWLINE":
                    tokens.append((kind, match.group()))
                pos += len(match.group())
                break
        else:
            raise SyntaxError(f"رمز غير معروف: {code[pos]}")
    return tokens
