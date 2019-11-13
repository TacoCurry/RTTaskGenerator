class Memories:
    mem_list = []
    mem_type = ''
    capacity= ''
    wcet_scale= ''
    power_active= ''
    power_idle= ''
    def insert_memory(self,mem_type, capacity, wcet_scale, power_active, power_idle) -> bool:
        self.mem_type = mem_type
        self.capacity = capacity
        self.power_active = power_active
        self.power_idle = power_idle
        self.wcet_scale = wcet_scale







