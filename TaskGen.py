import random
from Input import InputUtils
from Memory import Memory
from Memory import Memories
from Task import Task
class GenTask:
    def __init__(self):
        self.util_cpu_1task = Task.util_cpu / Task.n_tasks
        self.util_mem_1task = self.get_mem_util() /Task.n_tasks
        self.util_bymem = Task.util_target - Task.util_cpu
        self.util_mem = 1.0 / Memories.n_mem_types

    def get_mem_util(self):
        if self.util_bymem > 0:
            for i in range (Memories.n_mem_types):
                self.util_overhead = 1 / Memories.list[i].wcet_scale - 1
            if self.util_overhead< self.util_bymem:
                self.util_bymem -= self.util_overhead
                self.util_mem += 1.0/Memories.n_mem_types
            else:
                self.util_mem += 1.0 / Memories.n_mem_types * self.util_bymem / self.util_overhead
                breakpoint()
        return self.util_mem




