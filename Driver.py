from SimConstants import Const

class Driver:

    def __init__(self, name, time, arrival_time, direction_from, direction_to, is_human):
        self.name = name
        self.is_human = is_human
        self.event = Const.ARRIVAL
        self.start_time = time
        self.direction_from = direction_from
        self.direction_to = direction_to
        self.elapsed_time = 0
        self.busy_time = arrival_time

    def get_from_to(self):
        return [self.direction_from, self.direction_to]