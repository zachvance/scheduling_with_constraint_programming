

class Job:
    def __init__(self, id, job, start_time, end_time, value, priority):
        self.id = id
        self.job = job
        self.start_time = start_time
        self.end_time = end_time
        self.value = value
        self.priority = priority


class Group:
    def __init__(self, group, jobs):
        self.group = group
        self.jobs = jobs
