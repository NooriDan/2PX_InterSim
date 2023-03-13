# External Libraries
import random
import time


# Custom Libraries
import Driver
import DriverQueue
from SimConstants import Const

ARRIVAL = "Arrival"
STOP = "Stop"
CLEAR = "Clear"

#   Directions:
N = "North"
E = "East"
S = "South"
W = "West"

#Classes
class Simulation:

    def __init__(self, total_cars):
        self.num_cars = 0
        self.total_cars = total_cars
        self.clock = 0

        self.intersection_free = True
        self.driver_queue = DriverQueue()
        self.generate_arrivals()
        self.completed_cars = []

    def run(self):
        while len(self.completed_cars) < self.total_cars:
            #print("The current time is ", self.clock)
            self.execute_events()
            self.driver_queue.elapse_driver_time()
            self.clock += Const.TIME_STEP
            
    def execute_events(self):
        for driver in self.driver_queue.intersection:
            if driver.busy_time <= 0:
                self.execute_clear(driver)
        for driver in self.driver_queue.north:
            if driver.busy_time <= 0:
                self.execute_arrival(driver)
        for driver in self.driver_queue.west:
            if driver.busy_time <= 0:
                self.execute_arrival(driver)
        for driver in self.driver_queue.south:
            if driver.busy_time <= 0:
                self.execute_arrival(driver)
        for driver in self.driver_queue.east:
            if driver.busy_time <= 0:
                self.execute_arrival(driver)

        driver = self.driver_queue.get_next_driver()
        if driver != None:
            self.execute_stop(driver)
            
        if self.num_cars < self.total_cars:
            self.generate_arrivals()

    def execute_arrival(self, driver):
        desire = driver.get_from_to()

        if desire[0] == N:
            driver.event = STOP
            if driver.is_human:
                driver.busy_time = Const.HUMAN_MIN_STOP_TIME
            else:
                driver.busy_time = Const.SDC_MIN_STOP_TIME
            self.driver_queue.north.pop(0)
            self.driver_queue.add_driver_stop(driver)
        elif desire[0] == S:
            driver.event = STOP
            if driver.is_human:
                driver.busy_time = Const.HUMAN_MIN_STOP_TIME
            else:
                driver.busy_time = Const.SDC_MIN_STOP_TIME
            self.driver_queue.south.pop(0)
            self.driver_queue.add_driver_stop(driver)
        elif desire[0] == E:
            driver.event = STOP
            if driver.is_human:
                driver.busy_time = Const.HUMAN_MIN_STOP_TIME
            else:
                driver.busy_time = Const.SDC_MIN_STOP_TIME
            self.driver_queue.east.pop(0)
            self.driver_queue.add_driver_stop(driver)
        elif desire[0] == W:
            driver.event = STOP
            if driver.is_human:
                driver.busy_time = Const.HUMAN_MIN_STOP_TIME
            else:
                driver.busy_time = Const.SDC_MIN_STOP_TIME
            self.driver_queue.west.pop(0)
            self.driver_queue.add_driver_stop(driver)

          
    def generate_arrivals(self):
        time = self.clock
        
        r = random.random()
        car_id = self.num_cars
        if r < Const.NORTH_CAR_PROBABILITY and len(self.driver_queue.north) == 0: #From North
            r = random.random()
            if r < Const.TURN_PROBABILITY:
                r = random.random()
                if r < Const.LEFT_TURN_PROBABILITY:
                    direction_to = E
                else:
                    direction_to = W
            else:
                direction_to = S
            r = random.random()
            if r < Const.HUMAN_PROBABILITY:
                is_human = True
            else:
                is_human = False
            #print("Driver ", car_id, " from the North is going to the ", direction_to)
            self.driver_queue.add_driver_arrivals(Driver(car_id, time, Const.ARRIVAL_TIME, N, direction_to, is_human))
            self.num_cars += 1

        r = random.random()
        car_id = self.num_cars
        if r < Const.EAST_CAR_PROBABILITY and len(self.driver_queue.east) == 0: #From East
            r = random.random()
            if r < Const.TURN_PROBABILITY:
                r = random.random()
                if r < Const.LEFT_TURN_PROBABILITY:
                    direction_to = S
                else:
                    direction_to = N
            else:
                direction_to = W
            r = random.random()
            if r < Const.HUMAN_PROBABILITY:
                is_human = True
            else:
                is_human = False
            #print("Driver ", car_id, " from the East is going to the ", direction_to)
            self.driver_queue.add_driver_arrivals(Driver(car_id, time, Const.ARRIVAL_TIME, E, direction_to, is_human))
            self.num_cars += 1

        r = random.random()
        car_id = self.num_cars
        if r < Const.SOUTH_CAR_PROBABILITY and len(self.driver_queue.south) == 0: #From South
            r = random.random()
            if r < Const.TURN_PROBABILITY:
                r = random.random()
                if r < Const.LEFT_TURN_PROBABILITY:
                    direction_to = W
                else:
                    direction_to = E
            else:
                direction_to = N
            r = random.random()
            if r < Const.HUMAN_PROBABILITY:
                is_human = True
            else:
                is_human = False
            #print("Driver ", car_id, " from the South is going to the ", direction_to)
            self.driver_queue.add_driver_arrivals(Driver(car_id, time, Const.ARRIVAL_TIME, S, direction_to, is_human))
            self.num_cars += 1

        r = random.random()
        car_id = self.num_cars
        if r < Const.WEST_CAR_PROBABILITY and len(self.driver_queue.west) == 0: #From West
            r = random.random()
            if r < Const.TURN_PROBABILITY:
                r = random.random()
                if r < Const.LEFT_TURN_PROBABILITY:
                    direction_to = N
                else:
                    direction_to = S
            else:
                direction_to = E
            r = random.random()
            if r < Const.HUMAN_PROBABILITY:
                is_human = True
            else:
                is_human = False
            #print("Driver ", car_id, "from the West is going to the ", direction_to)
            self.driver_queue.add_driver_arrivals(Driver(car_id, time, Const.ARRIVAL_TIME, W, direction_to, is_human))
            self.num_cars += 1

    def execute_clear(self, driver):
        driver.elapsed_time = self.clock - driver.start_time
        self.completed_cars.append(driver)
        self.driver_queue.intersection.pop(0)
        #print("Driver ", driver.name, " just left the intersection after ", driver.elapsed_time, "seconds")
        if len(self.driver_queue.intersection) == 0:
            self.intersection_free = True

    def execute_stop(self, driver):
        desire = driver.get_from_to()
        if not self.intersection_free:
            return


        if desire[0] == N and self.intersection_free:
            if desire[1] == S:
                driver.event = CLEAR
                if driver.is_human:
                    driver.busy_time = Const.HUMAN_CLEAR_TIME
                else:
                    driver.busy_time = Const.SDC_CLEAR_TIME
                self.driver_queue.north_stop.pop(0)
                self.driver_queue.reset_busy_time(N)
                self.driver_queue.add_driver_intersection(driver)
                self.intersection_free = False
            else:
                driver.event = CLEAR
                if driver.is_human:
                    driver.busy_time = Const.HUMAN_TURNING_TIME
                else:
                    driver.busy_time = Const.SDC_TURNING_TIME
                self.driver_queue.north_stop.pop(0)
                self.driver_queue.reset_busy_time(N)
                self.driver_queue.add_driver_intersection(driver)
                self.intersection_free = False
        elif desire[0] == S and self.intersection_free:
            if desire[1] == N:
                driver.event = CLEAR
                if driver.is_human:
                    driver.busy_time = Const.HUMAN_CLEAR_TIME
                else:
                    driver.busy_time = Const.SDC_CLEAR_TIME
                self.driver_queue.south_stop.pop(0)
                self.driver_queue.reset_busy_time(S)
                self.driver_queue.add_driver_intersection(driver)
                self.intersection_free = False
            else:
                driver.event = CLEAR
                if driver.is_human:
                    driver.busy_time = Const.HUMAN_TURNING_TIME
                else:
                    driver.busy_time = Const.SDC_TURNING_TIME
                self.driver_queue.south_stop.pop(0)
                self.driver_queue.reset_busy_time(S)
                self.driver_queue.add_driver_intersection(driver)
                self.intersection_free = False
        elif desire[0] == E and self.intersection_free:
            if desire[1] == W:
                driver.event = CLEAR
                if driver.is_human:
                    driver.busy_time = Const.HUMAN_CLEAR_TIME
                else:
                    driver.busy_time = Const.SDC_CLEAR_TIME
                self.driver_queue.east_stop.pop(0)
                self.driver_queue.reset_busy_time(E)
                self.driver_queue.add_driver_intersection(driver)
                self.intersection_free = False
            else:
                driver.event = CLEAR
                if driver.is_human:
                    driver.busy_time = Const.HUMAN_TURNING_TIME
                else:
                    driver.busy_time = Const.SDC_TURNING_TIME
                self.driver_queue.east_stop.pop(0)
                self.driver_queue.reset_busy_time(E)
                self.driver_queue.add_driver_intersection(driver)
                self.intersection_free = False
        elif desire[0] == W and self.intersection_free:
            if desire[1] == E:
                driver.event = CLEAR
                if driver.is_human:
                    driver.busy_time = Const.HUMAN_CLEAR_TIME
                else:
                    driver.busy_time = Const.SDC_CLEAR_TIME
                self.driver_queue.west_stop.pop(0)
                self.driver_queue.reset_busy_time(W)
                self.driver_queue.add_driver_intersection(driver)
                self.intersection_free = False
            else:
                driver.event = CLEAR
                if driver.is_human:
                    driver.busy_time = Const.HUMAN_TURNING_TIME
                else:
                    driver.busy_time = Const.SDC_TURNING_TIME
                self.driver_queue.west_stop.pop(0)
                self.driver_queue.reset_busy_time(W)
                self.driver_queue.add_driver_intersection(driver)
                self.intersection_free = False

    def output_times(self):
        times = []
        for car in self.completed_cars:
            times.append(car.elapsed_time)
        print(times)

    def output_to_CSV(self, name: str):
        f = open("results\_" + name + ".csv", 'w')
        f.write("Name,Type,Start Time,Elapsed Time,Start Direction,End Direction\n")
        for car in self.completed_cars:
            f.write(str(car.name) + "," + str(car.is_human) + "," + str(car.start_time) + "," + str(car.elapsed_time) + "," + str(car.direction_from) + "," + str(car.direction_to) + "\n")
        f.close()
        
