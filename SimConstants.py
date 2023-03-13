# Class of Constants


class Const:
    #   Event types:
    ARRIVAL = "Arrival"
    STOP = "Stop"
    CLEAR = "Clear"

    #   Directions:
    N = "North"
    E = "East"
    S = "South"
    W = "West"


    #   Controls
    TIME_STEP = .1
    ARRIVAL_TIME = 10
    HUMAN_CLEAR_TIME = 3
    SDC_CLEAR_TIME = 2
    HUMAN_TURNING_TIME = 5
    SDC_TURNING_TIME = 4
    HUMAN_MIN_STOP_TIME = 2
    SDC_MIN_STOP_TIME = 1


    NORTH_CAR_PROBABILITY = 0.05
    EAST_CAR_PROBABILITY = 0.05
    SOUTH_CAR_PROBABILITY = 0.05
    WEST_CAR_PROBABILITY = 0.05


    TURN_PROBABILITY = 0.33
    LEFT_TURN_PROBABILITY = 0.5
    HUMAN_PROBABILITY = 0.5