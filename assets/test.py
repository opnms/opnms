
from django_q.tasks import async, result

# create the task
async('math.copysign', 2, -2)

# or with import and storing the id
import math.copysign as copysign

task_id = async(copysign, 2, -2)

# get the result
task_result = result(task_id)

# result returns None if the task has not been executed yet
# you can wait for it
task_result = result(task_id, 200)

# but in most cases you will want to use a hook:

async('math.modf', 2.5, hook='hooks.print_result')

# hooks.py
def print_result(task):
    print(task.result)