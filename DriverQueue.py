import Driver
from SimConstants import Const

ARRIVAL = "Arrival"
STOP = "Stop"
CLEAR = "Clear"

#   Directions:
N = "North"
E = "East"
S = "South"
W = "West"

class DriverQueue:

    def __init__(self):
        self.north, self.east, self.south, self.west = [], [], [], []
        self.north_stop, self.east_stop, self.south_stop, self.west_stop = [], [], [], []
        self.intersection = []

    def add_driver_arrivals(self, driver):
        if driver.direction_from == N:
            self.north.append(driver)
        elif driver.direction_from == E:
            self.east.append(driver)
        elif driver.direction_from == S:
            self.south.append(driver)
        elif driver.direction_from == W:
            self.west.append(driver)

    def add_driver_stop(self, driver):
        if driver.direction_from == N:
            self.north_stop.append(driver)
        elif driver.direction_from == E:
            self.east_stop.append(driver)
        elif driver.direction_from == S:
            self.south_stop.append(driver)
        elif driver.direction_from == W:
            self.west_stop.append(driver)

    def add_driver_intersection(self, driver):
        self.intersection.append(driver)

    def elapse_driver_time(self):
        for driver in self.north:
            driver.busy_time -= Const.TIME_STEP
        for driver in self.east:
            driver.busy_time -= Const.TIME_STEP
        for driver in self.south:
            driver.busy_time -= Const.TIME_STEP
        for driver in self.west:
            driver.busy_time -= Const.TIME_STEP
        for driver in self.north_stop:
            driver.busy_time -= Const.TIME_STEP
        for driver in self.west_stop:
            driver.busy_time -= Const.TIME_STEP
        for driver in self.south_stop:
            driver.busy_time -= Const.TIME_STEP
        for driver in self.east_stop:
            driver.busy_time -= Const.TIME_STEP
        for driver in self.intersection:
            driver.busy_time -= Const.TIME_STEP

    def get_next_driver(self):
        min_busy_time = 0
        driver = None
        if len(self.north_stop) != 0 and self.north_stop[0].busy_time < min_busy_time:
            min_busy_time = self.north_stop[0].busy_time
            driver = self.north_stop[0]
        if len(self.east_stop) != 0 and self.east_stop[0].busy_time < min_busy_time:
            min_busy_time = self.east_stop[0].busy_time
            driver = self.east_stop[0]
        if len(self.south_stop) != 0 and self.south_stop[0].busy_time < min_busy_time:
            min_busy_time = self.south_stop[0].busy_time
            driver = self.south_stop[0]
        if len(self.west_stop) != 0 and self.west_stop[0].busy_time < min_busy_time:
            min_busy_time = self.west_stop[0].busy_time
            driver = self.west_stop[0]
        return driver

    def reset_busy_time(self, direction):
        if direction == N:
            for driver in self.north_stop:
                if driver.busy_time < 0:
                    driver.busy_time = 0
        elif direction == E:
            for driver in self.east_stop:
                if driver.busy_time < 0:
                    driver.busy_time = 0
        elif direction == S:
            for driver in self.south_stop:
                if driver.busy_time < 0:
                    driver.busy_time = 0
        elif direction == W:
            for driver in self.west_stop:
                if driver.busy_time < 0:
                    driver.busy_time = 0
        
