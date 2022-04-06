#!/usr/bin/env python3
r'''
 Canonical: https://github.com/lduran2/trafficSimulator/src/assignment02.py
 By        : Leomar Durán <https://github.com/lduran2>
 When      : 2022-04-06t19:15Q
 For       : CIS 4XXX/Introduction to Cyber-Physical Systems
 Version   : 2.0.1

 CHANGELOG :
    v2.0.1 - 2022-04-06t19:15Q
        following paths cyclically

    v2.0.0 - 2022-04-06t18:04Q
        squared curves

    v1.2.0 - 2022-03-30t23:17Q
        running some cars

    v1.1.0 - 2022-03-30t22:55Q
        connecting square roads

    v1.0.0 - 2022-03-30t22:27Q
        import all from traffic simulator
 '''
from trafficSimulator import *
from math import copysign

# radius of circle touching midpoints of the lines of the square track
r = 70

# radius of intersection
intersection_r = 0

# the roads, curves of the square track
roads = [
    ((-r - intersection_r, -r), (+r + intersection_r, -r)),
    ((+r, -r - intersection_r), (+r, +r + intersection_r)),
    ((+r + intersection_r, +r), (-r - intersection_r, +r)),
    ((-r, +r + intersection_r), (-r, -r - intersection_r))
]

vehicle_data = {
    r'vehicle_rate': 50,
    r'vehicles': [
        [1, {r'path': [0, 1, 2, 3, 0]}]
    ] * 50
}

# print the data so far
print('===roads===')
print(roads)
print('===vehicle data===')
print(vehicle_data)

# create a simulation
sim = Simulation()
sim.create_roads(roads)
sim.create_gen(vehicle_data)

# run the simulation
win = Window(sim)
win.offset = (0, 0)
win.run(steps_per_update=1)

# report done
print('Done.')
