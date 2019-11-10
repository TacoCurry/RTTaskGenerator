from Memory import Memories
from Task import Task
from TaskGen import GenTask

class InputUtils:

    @staticmethod
    def set_memory(input_file="input_mem.txt"):
        try:
            with open(input_file, "r", encoding='UTF8') as f:
                for i in range(2):
                    temp = f.readline().split()
                    Memories.insert_memory(memory_str=temp[0], capacity=int(temp[1]), wcet_scale=float(temp[2]),
                                                  power_active=float(temp[3]), power_idle=float(temp[4]))
        except FileNotFoundError:
            GenTask.error("memory 정보 파일을 찾을 수 없습니다.")

    @staticmethod
    def set_tasks(input_file="input_tasks.txt"):
        try:
            with open(input_file, "r", encoding='UTF8') as f:
                n_task = int(f.readline())
                for i in range(n_task):
                    temp = f.readline().split()
                    Task.append(Task(no=i+1, wcet_min=int(temp[0]), wcet_max=int(temp[1]), ###
                                             mem_total=int(temp[2]), util_cpu=float(temp[3]), util_target=float(temp[4])))
        except FileNotFoundError:
            GenTask.error("task 정보 파일을 찾을 수 없습니다.")