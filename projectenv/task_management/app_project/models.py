from django.db import models

class Worker(models.Model):
    first_name = models.CharField(max_length=70, null=True) 
    last_name = models.CharField(max_length=70, null=True) 
    fee_per_hour = models.IntegerField(null=True)
    salary = 0
    tasks = []

    def __str__(self):
        return self.last_name

class Task(models.Model):
    title = models.CharField(max_length=70, null=True) 
    workers = models.ManyToManyField(Worker, related_name='workers_set')
    duration = models.IntegerField(null=True) 
    manager = models.ForeignKey(Worker, on_delete=models.CASCADE, null=True, related_name='manager_set')

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=70, null=True) 
    task = models.ManyToManyField(Task) 
    start_date = models.DateField(null=True)  

    def __str__(self):
        return self.title
    
