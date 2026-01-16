class Scheduler:
    def __init__(self, entities):
        self.entities = entities

    def run_all(self):
        for e in self.entities:
            e.run()
