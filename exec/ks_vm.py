class KSVM:
    def __init__(self, ir_entity):
        self.entity = ir_entity

    def run(self):
        self.entity.state += self.entity.increment
        print(f"[{self.entity.name}] الحالة = {self.entity.state}")
