def analyze(ast):
    if ast.state < 0:
        raise ValueError("قيمة الحالة لا يمكن أن تكون سالبة")

    if ast.decision.increment == 0:
        raise ValueError("قرار بلا تأثير")
