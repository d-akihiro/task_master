from task_master import thread_manager


class OperateBase(object):
    def __init__(self, id_:str, lock_id_:str=None):
        self.id = id_
        self.lock_id = lock_id_
        self.is_abort = False

    def start(self):
        self.lock()
        try:
            if not self.is_abort():
                self.execute()
        finally:
            self.release()

    def lock(self):
        if self.lock_id:
            thread_manager.ThreadManager().lock(self.lock_id)

    def release(self):
        if self.lock_id:
            thread_manager.ThreadManager().release(self.lock_id)

    def abort(self):
        self.is_abort = True

    def is_abort(self):
        return self.is_abort

    def execute(self):
        pass

