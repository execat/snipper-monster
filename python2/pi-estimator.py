#!/usr/bin/env python
"""
From: http://davidshimel.com/approximating-pi-in-python-part-1/
Calculate the value of pi probablistically by calculating

pi = 4 * area of quadrant / area of 1/4th of the inscribing square OR
pi = 2 * area of quadrant / area of the 45-45-90 triangle inscribed in the quadrant

Instructions:
Pass the number of darts (larger the better) as a parameter.
"""

import random
import sys
 
def point_in_circle(x, y):
    return True if x**2 + y**2 <= 1 else False
 
def point_in_triangle(x, y):
    return True if x + y <= 1 else False # assume x and y are positive
 
def get_point():
    return random.random(), random.random()
 
def get_point_in_shapes():
    x, y = get_point()
    in_circle = point_in_circle(x, y)
    in_triangle = False
    if in_circle: # if the point isn't in the circle, we know that it can't be in the triangle
        in_triangle = point_in_triangle(x, y)
    return in_circle, in_triangle
 
def get_points_in_shapes(N_darts):
    N_circle, N_triangle = 0, 0
    i = 0 # keep track of how many darts we've thrown so far
    while i < N_darts:
        in_circle, in_triangle = get_point_in_shapes()
        if in_circle:
            N_circle += 1
        if in_triangle:
            N_triangle += 1
        i += 1
    return N_circle, N_triangle
 
def pi_formula(N_darts, N_circle):
    return 4.0 * N_circle / N_darts
 
def pi_formula2(N_darts, N_circle, N_triangle):
    if 0 == N_triangle: # if no darts landed in the triangle, avoid dividing by zero by falling
                # back on the equation that doesn't use the area of the triangle
        return pi_formula(N_darts, N_circle)
    # otherwise, average the two approximations
    return N_circle * (2.0 / N_darts + 1.0 / N_triangle)
 
def calculate_pi(N_darts):
    N_circle, N_triangle = get_points_in_shapes(N_darts)
    return pi_formula2(N_darts, N_circle, N_triangle)
 
# driver
N_darts = int(sys.argv[1]) # the total number of darts to throw (given by a command-line argument)
print calculate_pi(N_darts)
