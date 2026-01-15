import threading

class Lock:
    """
    قفل بسيط لاستخدامه في التعليمات LOCK / UNLOCK
    """

    def __init__(self):
        self._lock = threading.Lock()

    def acquire(self):
        self._lock.acquire()

    def release(self):
        self._lock.release()


class AtomicInteger:
    """
    عدد صحيح ذرّي (Atomic)
    """

    def __init__(self, value=0):
        self._value = value
        self._lock = threading.Lock()

    def get(self):
        with self._lock:
            return self._value

    def set(self, value):
        with self._lock:
            self._value = value

    def add(self, delta):
        with self._lock:
            self._value += delta
            return self._value
          
