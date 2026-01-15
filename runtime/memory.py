import threading

class Memory:
    """
    ذاكرة مشتركة بين جميع الأنوية
    مع حماية من التعارض (Race Conditions)
    """

    def __init__(self):
        self._heap = {}
        self._lock = threading.Lock()

    def load(self, address):
        """
        قراءة من الذاكرة
        """
        with self._lock:
            return self._heap.get(address, 0)

    def store(self, address, value):
        """
        كتابة إلى الذاكرة
        """
        with self._lock:
            self._heap[address] = value

    def dump(self):
        """
        (اختياري) تفريغ الذاكرة للتصحيح
        """
        with self._lock:
            return dict(self._heap)
          
