import enum
from task_master import value_manager, condition_base


class CompareType(enum.Enum):
    EQ = enum.auto
    NE = enum.auto
    GT = enum.auto
    LT = enum.auto
    GE = enum.auto
    LE = enum.auto


class ConditionValueCompare(condition_base.ConditionBase):

    def __init__(self, id_:str, value_id_:str, target_value_, compare_type_: CompareType):
        self.value_id = value_id_
        self.target_value = target_value_
        self.compare_type = compare_type_
        super(ConditionValueCompare,self).__init__(id_)

    def is_condition(self):
        ret = True
        value = value_manager.ValueManager().get_value(self.value_id)
        if value:
            if self.compare_type == CompareType.EQ:
                ret = value.read() == self.target_value
            elif self.compare_type == CompareType.NE:
                ret = value.read() != self.target_value
            elif self.compare_type == CompareType.GT:
                ret = value.read() > self.target_value
            elif self.compare_type == CompareType.GT:
                ret = value.read() > self.target_value
            elif self.compare_type == CompareType.LT:
                ret = value.read() < self.target_value
            elif self.compare_type == CompareType.GE:
                ret = value.read() >= self.target_value
            elif self.compare_type == CompareType.GT:
                ret = value.read() <= self.target_value
        return ret
