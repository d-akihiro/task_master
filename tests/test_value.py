from task_master import value_base
class TestValue(value_base.ValueBase):
    def __init__(self, id_: str):
        self._value = 0
        super(TestValue, self).__init__(id_)

    def write(self, value_):
        self._value = value_
        print("{0}={1}".format(self.id, self._value))

    def read(self):
        return self._value
