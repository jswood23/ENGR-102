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

# Part a)

def f_of_x(x):
    # original function was f = x**3 + 3*x**2 + 4*x + 5
    f = x**3 + 3*x**2 + 4*x + 5
    return f

# Part b)

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

# try print(deriv(5)) or any other number to test

# Part c)
def newton_step(num):
    approximation = num - (f_of_x(num) / deriv(num))
    return approximation

# Part d)
def newton(initial_guess):
    first_approximation = newton_step(initial_guess)
    next_approximation = newton_step(first_approximation)
    
    approximations = [initial_guess, first_approximation, next_approximation]
    diff = first_approximation - next_approximation
    while abs(diff) >= 1e-6:
        last_approximation = next_approximation
        next_approximation = newton_step(last_approximation)
        approximations.append(next_approximation)
        diff = last_approximation - next_approximation
    return approximations

# Part e)
# F = eval(input("Enter a function in appropriate Python syntax: "))
x0 = float(input("Enter the initial guess for a root of the function: "))
newton_values = newton(x0)
print("Successive root approximations:\n", newton_values)
print("The most accurate value found of the root of the function is ", round(newton_values[len(newton_values) - 1], 8))

# Part f)

# Part g)

# Challenge a)

# Challenge b)
