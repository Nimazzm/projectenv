class Project:
    def __init__(self, title, tasks, start_date):
        self.title = title
        self.tasks = tasks
        self.start_date = start_date

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return self.title
    
    @property
    def cost(self):
        return sum([task.cost for task in self.tasks]) 
    
    @property
    def duration(self):
        return sum([task.duration for task in self.tasks])