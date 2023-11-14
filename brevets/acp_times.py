import arrow
import math

brev_min = [[200, 15],
            [400, 15],
            [600, 15],
            [1000, 11.428],
            [1300, 13.333]]

brev_max = [[200, 34],
            [400, 32],
            [600, 30],
            [1000, 28],
            [1300, 26]]

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    if control_dist_km == 0:
        return brevet_start_time
    for distance, speed in brev_max:
        if control_dist_km <= distance:
            hours = control_dist_km / speed
            return brevet_start_time.shift(hours=hours)
    return "Error!"

def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    if control_dist_km == 0:
        return brevet_start_time.shift(hours=1)
    for distance, speed in brev_min:
        if control_dist_km <= distance:
            hours = control_dist_km / speed
            return brevet_start_time.shift(hours=hours)
    return "Error!"
