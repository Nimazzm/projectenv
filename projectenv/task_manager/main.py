from project import Project
from person import Worker
from task import Task
from datetime import datetime

if __name__ == '__main__':

    worker_1 = Worker('mohamad', 'sadeghi', 1)
    worker_2 = Worker('amir', 'fashami', 2)
    worker_3 = Worker('akbar', 'hassani', 2)
    worker_4 = Worker('alireza', 'kalaie', 1)

    task_1 = Task(title='takhrib', workers=[worker_1, worker_2], manager=worker_2, duration=10)
    task_2 = Task(title='tirahan', workers=[worker_3], manager=worker_3, duration=10)
    task_3 = Task(title='sakht', workers=[worker_3, worker_1, worker_4], manager=worker_3, duration=15)

    start_date = '2024-10-7'

    project_1 = Project(title='Iran mall', tasks=[task_1, task_2, task_3], start_date=datetime.strptime(start_date, '%Y-%m-%d'))


    print('project_1', project_1)
    print('projct_1.tasks: ', project_1.tasks)
    print('projct_1.start_date: ', project_1.start_date)
    print('projct_1.cost: ', project_1.cost)
    print('projct_1.duration: ', project_1.duration)
    print()
    print('task_1', task_1)
    print('task_1.workers', task_1.workers)
    print('task_1.manager', task_1.manager)
    print('task_1.duration', task_1.duration)
    print('task_1.cost', task_1.cost)
    print()
    print('task_2', task_2)
    print('task_2.workers', task_2.workers)
    print('task_2.manager', task_2.manager)
    print('task_2.duration', task_2.duration)
    print('task_2.cost', task_2.cost)
    print()
    print('task_3', task_3)
    print('task_3.workers', task_3.workers)
    print('task_3.manager', task_3.manager)
    print('task_3.duration', task_3.duration)
    print('task_3.cost', task_3.cost)
    print()
    print('worker_1.name', worker_1.fname, worker_1.lname)
    print('worker_1.salary', worker_1.salary)
    print('worker_1.task', worker_1.task)
    print('worker_2.name', worker_2.fname, worker_2.lname)
    print('worker_2.salary', worker_2.salary)
    print('worker_2.task', worker_2.task)
    print('worker_3.name', worker_3.fname, worker_3.lname)
    print('worker_3.salary', worker_3.salary)
    print('worker_3.task', worker_3.task)
