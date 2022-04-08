#!/usr/bin/env python3
r'''
 Canonical: https://github.com/lduran2/trafficSimulator/src/assignment02.py
 By        : Leomar Durán <https://github.com/lduran2>
 When      : 2022-04-06t19:43Q
 For       : CIS 4XXX/Introduction to Cyber-Physical Systems
 Version   : 2.1.0

 CHANGELOG :
    v2.1.0 - 2022-04-06t19:43Q
        different possible paths

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

# minimum number vehicles
N_VEHICLES = 50

# radius of circle touching midpoints of the lines of the square track
R = 70

# radius of intersection
INTERSECTION_R = 0

# ask whether to use case 2.
case2 = input('Use case #2 with the inner roads? [y, N otherwise]\n> ')

# the roads, curves of the square track
roads = [
    # outer roads
    ((-R - INTERSECTION_R, -R), (+R + INTERSECTION_R, -R)),
    ((+R, -R - INTERSECTION_R), (+R, +R + INTERSECTION_R)),
    ((+R + INTERSECTION_R, +R), (-R - INTERSECTION_R, +R)),
    ((-R, +R + INTERSECTION_R), (-R, -R - INTERSECTION_R))
]

inner_tracks = []

if (case2=='y' or case2=='Y'):
    roads = roads + [
        # add intersecting roads
        ((0, -R), (0, 0)),
        ((0, 0), (0, R)),
        ((R, 0), (0, 0)),
        ((0, 0), (-R, 0))
    ]
    inner_tracks = [
    [1, {r'path': [0, 4, 7, 3, 0]}],
        [1, {r'path': [0, 4, 5, 2, 3, 0]}],
        [1, {r'path': [1, 6, 7, 3, 0, 1]}],
        [1, {r'path': [1, 6, 5, 2, 3, 0, 1]}]
    ]
# end if (case2=='y' or case2=='Y')

# number roads
N_ROADS = len(roads)

vehicle_data = {
    r'vehicle_rate': N_VEHICLES,
    r'vehicles': [
        [1, {r'path': (list(range(4))*2)[0:][:5]}],
        [1, {r'path': (list(range(4))*2)[1:][:5]}],
        [1, {r'path': (list(range(4))*2)[2:][:5]}],
        [1, {r'path': (list(range(4))*2)[3:][:5]}],
        *inner_tracks
    ] * ((N_VEHICLES // (N_ROADS + 4)) + 1)
}

# print the data so far
print(r'===roads===')
print(roads)
print(r'===vehicle data===')
print(vehicle_data)

# ask for minimum perturbation
try:
    alpha = int(input('Please enter the minimum perturbation, [default to 1.0].\n> '))
except:
    # default to 1.0 on invalid integer
    alpha = 1.0
# end try int(input())

# create a simulation
sim = Simulation()
sim.create_roads(roads)
sim.create_gen(vehicle_data, alpha)

if (case2=='y' or case2=='Y'):
    # add the traffic signals if inner roads
    sim.create_signal([[4, 5], [6, 7]])
# end if (case2=='y' or case2=='Y')

# run the simulation
win = Window(sim)
win.offset = (0, 0)
win.run(steps_per_update=1)

# report done
print(r'Done.')
