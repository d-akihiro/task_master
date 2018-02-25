import time
from task_master import value_manager, operate_base


class TestOperate(operate_base.OperateBase):
    def __init__(self, value_id_:str, id_: str, lock_id_:str=None):
        self.value_id = value_id_

        super(TestOperate,self).__init__(id_, lock_id_)

    def execute(self):
        print("operate {0}". format(self.id))
        value = value_manager.ValueManager().get_value(self.value_id)
        value.write(value.read() + 1)
        time.sleep(1)
