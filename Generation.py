import sys
from Utility import Variables
from Utility import Nansu
from Utility import ErrorMsg
from Memory import Memories

util_cpu_1task = 0
util_mem_1task = 0
memreq_1task = 0
n_mems = 2



class GenTask:


    def gen_task(a):
        global util_cpu_1task
        util_cpu_1task = Variables.util_cpu / Variables.n_tasks
        global util_mem_1task
        util_mem_1task = GenTask.get_mem_util(1) / Variables.n_tasks;
        print(util_mem_1task)
        global memreq_1task
        memreq_1task = Variables.mem_total * util_mem_1task
        try:
            with open("task_generated.txt", "w", encoding='UTF8') as f:
                for i in range(Variables.n_tasks):
                    GenTask.do_gen_task(f)


        except FileNotFoundError:
            ErrorMsg.error("cannot open task_generated.txt")
        #print(f'full power utilization: {GenTask.get_util_overhead_bymem(memreq_total)}')

    @staticmethod
    def do_gen_task(input_file):
        global util_cpu_1task
        wcet = Variables.wcet_min + Nansu.get_rand(Variables.wcet_max - Variables.wcet_min)
        duration = wcet / util_cpu_1task
                   #+ (int)(Nansu.get_rand(wcet / util_cpu_1task/2)) - (int)(Nansu.get_rand(wcet / util_cpu_1task/2))
        print(wcet, duration)
        print(util_cpu_1task)

        input_file.write(str(wcet))

    @staticmethod
    def get_mem_util(a):
        global n_mems
        util_bymem = Variables.util_target - Variables.util_cpu
        util_mem = 1.0 / n_mems
        while(1):
            i=0
            i = i+1
            if(i < n_mems and util_bymem >0):
                break
            util_overhead = 1 / Memories.mem_list[i].wcet_scale - 1
            if(util_overhead<util_bymem):
                util_bymem -= util_overhead
                util_mem += 1.0 / n_mems
            else:
                util_mem += 1.0 / n_mems * util_bymem / util_overhead
                break

        return util_mem


    def get_util_overhead_bymem(mem_used):
            util_overhead = 0
            global n_mems
            mem_total_per_type = Variables.mem_total / n_mems
            for i in range(n_mems):
                overhead = 1 / Memories.mem_list[i].wcet_scale - 1
                if(mem_used < mem_total_per_type):
                    util_overhead += overhead * mem_used / mem_total_per_type
                    break
                else:
                    util_overhead += overhead
                    mem_used -= mem_total_per_type

            return util_overhead