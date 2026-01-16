from frontend.ast_nodes import EntityNode, DecisionNode

def parse(tokens):
    i = 0

    if tokens[i][0] != "ENTITY":
        raise SyntaxError("يجب أن يبدأ التعريف بكلمة كيان")
    i += 1

    name = tokens[i][1]
    i += 1

    if tokens[i][0] != "COLON":
        raise SyntaxError("متوقع ':' بعد اسم الكيان")
    i += 1

    # الحالة = NUMBER
    state_name = tokens[i][1]
    i += 2  # IDENT =
    state_value = int(tokens[i][1])
    i += 1

    # قرار :
    if tokens[i][0] != "DECISION":
        raise SyntaxError("متوقع قرار")
    i += 1

    if tokens[i][0] != "COLON":
        raise SyntaxError("متوقع ':' بعد قرار")
    i += 1

    # الحالة = الحالة + NUMBER
    target = tokens[i][1]
    i += 2  # IDENT =
    i += 2  # IDENT +
    increment = int(tokens[i][1])

    decision = DecisionNode(target, increment)
    return EntityNode(name, state_value, decision)
