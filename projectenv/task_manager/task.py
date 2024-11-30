class Task:
    def __init__(self, title, workers, duration, manager=[]):
        self.title = title 
        self.workers = workers
        self.duration = duration
        self.manager = manager
        
        hourly_task_duration = self.duration / len(self.workers)
        for worker in self.workers:
            if hasattr(worker, 'salary'):
                worker.salary += hourly_task_duration * worker.fee_per_hour
            else:
                worker.salary = hourly_task_duration * worker.fee_per_hour

        for worker in self.workers:
            if hasattr(worker, 'task'):
                worker.task += [self]
            else:
                worker.task = [self]

                
    def __str__(self):
        return self.title
    
    def __repr__(self):
        return self.title
    
    @property
    def cost(self):
        hourly_task_duration = self.duration / len(self.workers)
        res = 0
        for worker in self.workers:
            res += hourly_task_duration * worker.fee_per_hour
        return res