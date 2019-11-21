import random
import sys
class Variables:
    n_cores = 0
    n_tasks =0
    wcet_min = 0
    wcet_max = 0
    mem_total = 0
    util_cpu = 0
    total_mem_usage = 0


class Nansu:
    @staticmethod
    def get_rand(max_value):
        return random.randrange(int(max_value+1))

class ErrorMsg:
    @staticmethod
    def error(message: str):
        print(message)
        sys.exit()