import threading
import time
from task_master import thread_manager, task


class Work(threading.Thread):
    def __init__(self, sample_time_=1):
        super(Work, self).__init__()
        self._tasks = []
        self._initialy_task = []
        self._finaly_task = []
        self.abort_event = threading.Event()
        self.setDaemon(True)

        self.sample_time = sample_time_

        tm = thread_manager.ThreadManager()
        tm.append_thread(self)

    def append_initialy_task(self, task_: task.Task):
        self._initialy_task.append(task_)

    def append_finaly_task(self, task_: task.Task):
        self._finaly_task.append(task_)

    def append_task(self, task_: task.Task):
        self._tasks.append(task_)

    def run(self):
        ## Initialize
        while True:
            not_complete_tasks = []
            for task in self._initialy_task:
                if self.abort_event.is_set():
                    break
                if not task.is_complete_or_abort():
                    task.start()

            if len(not_complete_tasks) == 0:
                break

        for task in self._initialy_task:
            if self.abort_event.is_set():
                break

            if task.is_alive():
                task.join()

        while True:
            not_complete_tasks = []
            for task in self._tasks:
                if self.abort_event.is_set():
                    break

                if not task.is_complete_or_abort():
                    not_complete_tasks.append(task)
                    task.start()

            if len(not_complete_tasks) == 0:
                break

            time.sleep(self.sample_time)

        ## Finally
        while True:
            not_complete_tasks = []
            for task in self._finaly_task:
                if self.abort_event.is_set():
                    break
                if not task.is_complete_or_abort():
                    task.start()

            if len(not_complete_tasks) == 0:
                break

        for task in self._finaly_task:
            if self.abort_event.is_set():
                break

            if task.is_alive():
                task.join()

    def abort(self):
        self.abort_event.set()
        for task in self._initialy_task:
            task.abort()

        for task in self._tasks:
            task.abort()

        for task in self._finaly_task:
            task.abort()
