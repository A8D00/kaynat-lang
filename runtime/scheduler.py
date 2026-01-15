import threading
import queue
import os

class Scheduler:
    """
    Scheduler مسؤول عن:
    - توزيع المهام (Tasks)
    - تشغيلها على عدة أنوية (Threads)
    """

    def __init__(self, cores=None):
        # إذا لم يُحدد عدد الأنوية → استخدم عدد أنوية الجهاز
        self.cores = cores or os.cpu_count() or 1
        self.task_queue = queue.Queue()
        self.threads = []

    def submit(self, task):
        """
        إضافة مهمة (دالة) إلى قائمة التنفيذ
        """
        self.task_queue.put(task)

    def _worker(self):
        """
        نواة تنفيذ واحدة
        """
        while True:
            try:
                task = self.task_queue.get_nowait()
            except queue.Empty:
                break

            try:
                task()
            finally:
                self.task_queue.task_done()

    def run(self):
        """
        تشغيل جميع المهام على الأنوية
        """
        for _ in range(self.cores):
            t = threading.Thread(target=self._worker)
            t.start()
            self.threads.append(t)

        for t in self.threads:
            t.join()
