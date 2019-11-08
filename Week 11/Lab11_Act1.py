# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Josh Wood
# Justin Compton
# Braden Alexander
# Troy Hays
# Course/Section: ENGR 102-522
# Assignment: Lab11 Act1
# Date: 4 November 2019

from math import *

def f_of_x(x):
    # original function was f = x**3 + 3*x**2 + 4*x
    f = x**3 + 3*x**2 + 4*x
    return f

def deriv(x):
    tolerance = 1e-6
    h = 1
    lim = 1
    dfdx = (f_of_x(x + h) - f_of_x(x)) / h
    while lim > tolerance:
        h /= 2
        dfdx1 = (f_of_x(x + h) - f_of_x(x)) / h
        lim = abs(dfdx1 - dfdx)
        dfdx = dfdx1
    return round(dfdx, 2)

print(deriv(5))

