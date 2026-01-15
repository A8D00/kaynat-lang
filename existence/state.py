class State:
    def __init__(self, value=0):
        self.value = value

    def evolve(self, delta):
        self.value += delta
