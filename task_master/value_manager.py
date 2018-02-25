from task_master import value_base

class ValueManager(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ValueManager, cls).__new__(cls, *args, **kwargs)
            cls._values = {}
        return cls._instance

    def append_value(self, value_: value_base.ValueBase):
        self._values[value_.id] = value_

    def get_value(self, id_: str) -> value_base.ValueBase:
        if id_ in self._values:
            return self._values[id_]
        return None
