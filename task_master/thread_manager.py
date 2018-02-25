import threading

class ThreadManager(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ThreadManager, cls).__new__(cls, *args, **kwargs)
            cls._threads = []
            cls._locks = {}
        return cls._instance

    def clear(self, timeout):
        self.all_release()
        self.all_abort(timeout)

        self._threads.clear()
        self._locks.clear()

    def append_thread(self, thread_: threading.Thread):
        self._threads.append(thread_)

    def all_abort(self, timeout=None):
        for th in self._threads:
            th.abort()
        for th in self._threads:
            th.join(timeout)

    def lock(self, id_: str, timeout=-1):
        if not id_ in self._locks:
            self._locks[id_] = l = threading.Lock()
        print("lock {0}".format(id_))
        lock_obj = self._locks[id_]
        lock_obj.acquire(True, timeout)

    def release(self, id_:str):
        if id_ in self._locks:
            print("release {0}".format(id_))
            self._locks[id_].release()

    def all_release(self):
        for lk in self._locks:
            lk.release()