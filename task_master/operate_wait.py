import time
from task_master import operate_base

class OperateWait(operate_base.OperateBase):
    def __init__(self, id_:str, wait_time_):
        super(OperateWait, self).__init__(id_)
        self._wait_time = wait_time_

    def execute(self):
        time.sleep(self._wait_time)