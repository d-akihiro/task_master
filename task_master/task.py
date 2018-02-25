import threading
from task_master import thread_manager, condition_base, operate_base


class Task(threading.Thread):
    def __init__(self, id_:str, start_condition_:condition_base.ConditionBase=None, end_condition_:condition_base.ConditionBase=None):
        super(Task,self).__init__()
        self.id = id_
        self.operates = []
        self.abort_event = threading.Event()
        self.setDaemon(True)
        self.complete_event = threading.Event()

        self._start_condition = start_condition_
        self._end_condition = end_condition_

        tm = thread_manager.ThreadManager()
        tm.append_thread(self)

    def add_operate(self, operate_: operate_base.OperateBase):
        self.operates.append(operate_)

    def execute(self):
        while True:
            for op in self.operates:
                if not self.abort_event.is_set():
                    op.execute()

            if not self._end_condition or self._end_condition.is_condition():
                break

    def run(self):
        try:
            self.execute()
        finally:
            self.complete_event.set()

    def abort(self):
        self.abort_event.set()
        for op in self.operates:
            op.abort()

    def is_complete_or_abort(self):
        return self.abort_event.is_set() or self.complete_event.is_set()
    
    def start(self):
        if not self.is_alive():
            if not self._start_condition or self._start_condition.is_condition():
                super(Task, self).start()
