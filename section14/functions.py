'''def state_of_water (temp):
    if temp <= 0:
        return "Solid"
    elif 0 < temp < 100:
        return "lquid"
    else:
        return "Gas"'''
FREEZING_POINT = 0
BOILING_POINT = 100
def state_of_water (temp):
    if temp <= FREEZING_POINT:
        return "solid"
    elif FREEZING_POINT < temp < BOILING_POINT:
        return "liquid"
    else:
        return "Gas"

