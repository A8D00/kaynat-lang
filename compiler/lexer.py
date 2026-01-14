# lexer.py
# Lexer أولي للغة الكيانات

import sys

KEYWORDS = {
    "دالة",
    "أرجع",
    "إذا",
    "وإلا",
    "طالما"
}

class Token:
    def __init__(self, kind, value):
        self.kind = kind
        self.value = value

    def __repr__(self):
        return f"{self.kind}({self.value})"

def tokenize(source):
    tokens = []
    i = 0

    while i < len(source):
        ch = source[i]

        # تجاهل المسافات
        if ch.isspace():
            i += 1
            continue

        # أرقام
        if ch.isdigit():
            num = ch
            i += 1
            while i < len(source) and (source[i].isdigit() or source[i] == "٫"):
                num += source[i]
                i += 1
            tokens.append(Token("NUMBER", num))
            continue

        # نص
        if ch == '"':
            i += 1
            text = ""
            while i < len(source) and source[i] != '"':
                text += source[i]
                i += 1
            i += 1
            tokens.append(Token("STRING", text))
            continue

        # معرفات / كلمات محجوزة (عربي)
        if ch.isalpha():
            ident = ch
            i += 1
            while i < len(source) and source[i].isalpha():
                ident += source[i]
                i += 1

            if ident in KEYWORDS:
                tokens.append(Token("KEYWORD", ident))
            else:
                tokens.append(Token("IDENT", ident))
            continue

        # رموز
        tokens.append(Token("SYMBOL", ch))
        i += 1

    return tokens

if __name__ == "__main__":
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        src = f.read()

    for t in tokenize(src):
        print(t)
