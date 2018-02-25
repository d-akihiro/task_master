from tests import test_operate, test_value
import time
from task_master import value_manager, condition_value_compare, work, task, operate_wait

vm = value_manager.ValueManager()

value1 = test_value.TestValue("value1")
value2 = test_value.TestValue("value2")

vm.append_value(value1)
vm.append_value(value2)

op1 = test_operate.TestOperate(value1.id, "test1", "value1")

op2 = test_operate.TestOperate(value2.id, "test2")

op3 = operate_wait.OperateWait("wait", 1)

init_t1 = task.Task("Init_Task1")
init_t1.add_operate(op1)
init_t1.add_operate(op2)

init_t2 = task.Task("Init_Task2")
init_t2.add_operate(op1)
init_t2.add_operate(op2)

fin_t1 = task.Task("Fin_Task1")
fin_t1.add_operate(op1)
fin_t1.add_operate(op2)

fin_t2 = task.Task("Fin_Task2")
fin_t2.add_operate(op1)
fin_t2.add_operate(op2)

cd = condition_value_compare.ConditionValueCompare("value1_EQ_10", "value1", 10, condition_value_compare.CompareType.EQ)
t1 = task.Task("Task1", cd)

t1.add_operate(op1)
t1.add_operate(op1)
t1.add_operate(op1)
t1.add_operate(op1)
t1.add_operate(op1)
t1.add_operate(op2)

cd1 = condition_value_compare.ConditionValueCompare("value1_EQ_13", "value1", 13, condition_value_compare.CompareType.EQ)
cd2 = condition_value_compare.ConditionValueCompare("value1_EQ_13", "value1", 20, condition_value_compare.CompareType.EQ)
t2 = task.Task("Task2", cd1, cd2)

t2.add_operate(op1)
t2.add_operate(op3)

wk = work.Work()
wk.append_initialy_task(init_t1)
wk.append_initialy_task(init_t2)

wk.append_task(t1)
wk.append_task(t2)

wk.append_finaly_task(fin_t1)
wk.append_finaly_task(fin_t2)

wk.start()

time.sleep(3)
value1.write(10)
wk.join()
