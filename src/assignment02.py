#!/usr/bin/env python3
r'''
 Canonical: https://github.com/lduran2/trafficSimulator/src/assignment02.py
 By        : Leomar Durán <https://github.com/lduran2>
 When      : 2022-03-30t23:17Q
 For       : CIS 4XXX/Introduction to Cyber-Physical Systems
 Version   : 1.2.0

 CHANGELOG :
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
intersection_r = 10

# the roads, curves of the square track
roads = []
curves = []

# negative or positive
signs = (-1, 1)

# for each opposite corner
for opp in signs:
    # for each adjacent corner
    for adj in signs:
        # calculate centers of intersections
        # flat matrix
        (cx0, cy0, cx1, cy1) = (opp*r, opp*r, -adj*opp*r, adj*opp*r)
        # calculate distances of the intersections
        (dx, dy) = (cx1 - cx0, cy1 - cy0)
        # calculate box edges
        bx0 = cx0 + copysign(intersection_r, dx)*(dx != 0)
        bx1 = cx1 - copysign(intersection_r, dx)*(dx != 0)
        by0 = cy0 + copysign(intersection_r, dy)*(dy != 0)
        by1 = cy1 - copysign(intersection_r, dy)*(dy != 0)
        # add the road
        roads = roads + [((bx0, by0), (bx1, by1))]
# next adj, opp

# for each sign of x
for xsgn in signs:
    for ysgn in  signs:
        curves = curves + [(xsgn*r, ysgn*r)]
# next ysgn, xsgn

vehicle_data = {
    r'vehicle_rate': 50,
    r'vehicles': [
        [1, {r'path': [3, 2]}],
        [1, {r'path': [0]}],
        [1, {r'path': [1]}]
    ]
}

# print the data so far
print('===roads===')
print(roads)
print('===curves===')
print(curves)
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
