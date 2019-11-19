import sys
from Utility import Variables
from Utility import Nansu
from Utility import ErrorMsg
from Memory import Memories

util_cpu_1task = 0
util_mem_1task = 0
memreq_1task = 0
n_mems = 2

memreq_total = 0
util_sum_cpu = 0
memreq_total = 0

class GenTask:

    def gen_task(a):
        global util_cpu_1task
        util_cpu_1task = Variables.util_cpu / Variables.n_tasks
        global util_mem_1task
        util_mem_1task = GenTask.get_mem_util() / Variables.n_tasks;
        global memreq_1task
        memreq_1task = Variables.mem_total * util_mem_1task

        print("=======================================================")

        print(f'util_cpu_1task:{format(util_cpu_1task, ".6f")}')
        print(f'util_mem_1task: {format(util_mem_1task, ".6f")}')
        print(f'get_mem_util(): {format(GenTask.get_mem_util(),".6f")}')
        print(f'memreq_1task: {format(memreq_1task, ".0f")}')

        print("=======================================================")

        try:
            with open("task_generated.txt", "w", encoding='UTF8') as f:
                f.write("wcet duration memreq mem_active_ratio\n")
                for i in range(Variables.n_tasks):
                    print("--------------------------")
                    print(f'Task Number: {i+1}')
                    GenTask.do_gen_task(f)
                    print("--------------------------")



        except FileNotFoundError:
            ErrorMsg.error("cannot open task_generated.txt")

        print(f'full power utilization: {format(util_sum_cpu + GenTask.get_util_overhead_bymem(memreq_total),".6f")}')
        print(f'util_sum_mem: {format(GenTask.get_util_overhead_bymem(memreq_total), ".6f")}')
        print(f'util_sum_cpu: {format(util_sum_cpu, ".6f")}')
        print(f'memreq_total: {format(memreq_total, ".0f")}')


    @staticmethod
    def do_gen_task(input_file):
        global util_cpu_1task
        wcet = Variables.wcet_min + Nansu.get_rand(Variables.wcet_max - Variables.wcet_min)
        duration = wcet / util_cpu_1task + (int)(Nansu.get_rand(wcet / util_cpu_1task/2)) - (int)(Nansu.get_rand(wcet / util_cpu_1task/2))
        global memreq_1task
        memreq = memreq_1task + (int)(Nansu.get_rand(memreq_1task / 2))- (int)(Nansu.get_rand(memreq_1task / 2))

        mem_active_ratio = 0.1 + Nansu.get_rand(1000) / 10000.0 - Nansu.get_rand(1000) / 10000.0

        global util_sum_cpu
        util_sum_cpu += wcet / duration

        global memreq_total
        memreq_total += memreq

        line = f'{wcet} {format(duration,".0f")} {format(memreq,".0f")} {format(mem_active_ratio,".6f")}\n'
        print(f'util_sum_mem: {format(GenTask.get_util_overhead_bymem(memreq_total), ".6f")}')
        print(f'util_sum_cpu: {format(util_sum_cpu, ".6f")}')


        print(f'memreq_total: {format(memreq_total, ".0f")}')

        input_file.write(line)



    @staticmethod
    def get_mem_util() -> float:
        global n_mems
        util_bymem = Variables.util_target - Variables.util_cpu
        util_mem = 1.0 / n_mems

        for i in range(1,int(n_mems)):
            util_overhead = 1 / Memories.mem_list[i].wcet_scale - 1
            if util_bymem <= 0:
                break
            if util_overhead < util_bymem:
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