class Job:
    def __init__(self, job_id, job, start_time, end_time, value, priority):
        self.job_id = job_id
        self.job = job
        self.start_time = start_time
        self.end_time = end_time
        self.value = value
        self.priority = priority


class Group:
    def __init__(self, group_id: int):
        self.group_id = group_id
