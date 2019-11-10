class Task:
    def __init__(self,  wcet_min, wcet_max, mem_total, util_cpu, util_target, n_tasks):
        self.wcet_min = wcet_min
        self.wcet_max = wcet_max
        self.mem_total = mem_total
        self.util_cpu = util_cpu
        self.util_target = util_target
        self.n_tasks = n_tasks
