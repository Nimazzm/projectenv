from django.shortcuts import render
from .models import Task, Project, Worker

def home(request):
    return render(request, 'home.html', {})

def task(request):
    tasks = Task.objects.all()
    workers = Worker.objects.all()
    for task in tasks:
        hourly_task_duration = task.duration / len(task.workers)
        for worker in workers:
            if hasattr(worker, 'salary'):
                worker.salary += hourly_task_duration * worker.fee_per_hour
            else:
                worker.salary = hourly_task_duration * worker.fee_per_hour


    for worker in workers:
        if hasattr(worker, 'task'):
            worker.task += [worker]
        else:
            worker.task = [worker]



    tasks = Task.objects.all()
    workers = Worker.objects.all()
    for task in tasks:
        hourly_task_duration = task.duration / len(task.workers)
        cost = 0
        for worker in workers:
            cost += hourly_task_duration * worker.fee_per_hour
        return cost



    return render(request, 'task.html', {'cost':cost, 'salary':worker.salary, 'task':worker.task})



def project(request):
    projects = Project.objects.all()
    for project in projects:
        cost = sum([task.cost for task in project.task]) 
        duration =  sum([task.duration for task in project.task])
    

    return render(request, 'project.html', {'cost':cost, 'duration':duration})