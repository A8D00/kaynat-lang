import threading

class Memory:
    def __init__(self):
        # الذاكرة العامة (Heap)
        self.heap = {}
        self.lock = threading.Lock()

    def load(self, address):
        """
        قراءة قيمة من الذاكرة
        """
        with self.lock:
            return self.heap.get(address, 0)

    def store(self, address, value):
        """
        كتابة قيمة إلى الذاكرة
        """
        with self.lock:
            self.heap[address] = value

    def dump(self):
        """
        (اختياري) تفريغ الذاكرة لأغراض التصحيح
        """
        with self.lock:
            return dict(self.heap)
