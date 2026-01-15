import threading
import queue
import os

class Scheduler:
    def __init__(self, cores=None):
        # عدد الأنوية الافتراضي = عدد أنوية الجهاز
        self.cores = cores or os.cpu_count()
        self.tasks = queue.Queue()
        self.threads = []

    def submit(self, task):
        """
        إضافة مهمة (دالة) إلى المجدول
        """
        self.tasks.put(task)

    def worker(self, core_id):
        """
        حلقة تنفيذ لكل نواة
        """
        while True:
            try:
                task = self.tasks.get_nowait()
            except queue.Empty:
                break

            try:
                task()
            except Exception as e:
                print(f"[Core {core_id}] خطأ أثناء التنفيذ:", e)

            self.tasks.task_done()

    def run(self):
        """
        تشغيل المجدول على جميع الأنوية
        """
        for core_id in range(self.cores):
            t = threading.Thread(
                target=self.worker,
                args=(core_id,),
                daemon=True
            )
            t.start()
            self.threads.append(t)

        for t in self.threads:
            t.join()
