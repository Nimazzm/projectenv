class Worker:
    def __init__(self, fname, lname, fee_per_hour):
        self.fname = fname
        self.lname = lname
        self.fee_per_hour = fee_per_hour
        self.salary = 0
        self.task = []

    def __str__(self):
        return self.lname
    
    def __repr__(self):
        return self.lname