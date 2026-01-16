class EntityNode:
    def __init__(self, name, state, decision):
        self.name = name
        self.state = state
        self.decision = decision

class DecisionNode:
    def __init__(self, target, increment):
        self.target = target
        self.increment = increment
