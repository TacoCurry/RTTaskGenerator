import random
from Input import InputUtils
from Memory import Memory
from Memory import Memories
from Task import Task
import sys


class GenTask:
    def __init__(self):
        self.util_cpu_1task = Task.util_cpu / Task.n_tasks
        self.util_mem_1task = self.get_mem_util() /Task.n_tasks

        self.memreq_1task = Task.mem_total * self.util_mem_1task;

        self.util_bymem = Task.util_target - Task.util_cpu
        self.util_mem = 1.0 / Memories.n_mem_types
        self.util_sum_cpu = 0

        self.memreq_total = 0
        self.wcet = 0
        self.duration = 0.0
        self.memreq = 0
        self.mem_active_ratio = 0


    def makeTask(self):
        InputUtils.set_memory(self)
        InputUtils.set_tasks(self)
        fp = open("task_generated.txt", mode= 'w')
        if fp == None:
            GenTask.error("cannot open task_generated.txt")
        for i in range(Task.n_tasks):
            self.do_Gen_Task()
        fp.close
        print(f'\nfull power utilization: {self.util_sum_cpu + self.get_util_overhead_bymem(self.memreq_total)}')



    @staticmethod
    def do_Gen_Task(self, input_file= makeTask().fp):
        self.wcet = Task.wcet_min + random(Task.wcet_max - Task.wcet_min + 1)
        self.duration = (self.wcet / self.util_cpu_1task); + random(self.duration / 2) - random(self.duration / 2);
        self.memreq = self.memreq_1task + random(self.memreq_1task / 2) - random(self.memreq_1task / 2);
        self.mem_active_ratio = 0.1 + random(1000) / 10000.0 - random(1000) / 10000.0
        self.util_sum_cpu += self.wcet / self.duration
        self.memreq_total+= self.memreq
        input_file.write( self.wcet, self.duration, self.memreq, self.mem_active_ratio)

    @staticmethod
    def get_mem_util(self):
        if self.util_bymem > 0:
            for i in range (Memories.n_mem_types):
                util_overhead = 1 / Memories.list[i].wcet_scale - 1
                if util_overhead< self.util_bymem:
                    self.util_bymem -= util_overhead
                    self.util_mem += 1.0/Memories.n_mem_types
                else:
                    self.util_mem += 1.0 / Memories.n_mem_types * self.util_bymem / util_overhead
                    break
        return self.util_mem

    @staticmethod
    def error(self, message: str):
        print(message)
        sys.exit()

    @staticmethod
    def get_util_overhead_bymem(self, mem_used: int):
        util_overhead = 0
        self.mem_total_per_type = Task.mem_total / Memories.n_mem_types
        for i in range(Memories.n_mem_types):
            overhead = 1 / Memories.list[i].wcet_scale - 1
            if mem_used < self.mem_total_per_type:
                self.util_overhead += overhead * (mem_used / self.mem_total_per_type);
                break
            else:
                util_overhead += overhead
                mem_used -= self.mem_total_per_type
        return util_overhead

