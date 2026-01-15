class Pattern:
    def __init__(self, delta=1):
        self.delta = delta

    def evolve(self):
        self.delta += 1
