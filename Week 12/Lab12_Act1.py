# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Josh Wood
# Justin Compton
# Braden Alexander
# Troy Hays
# Course/Section: ENGR 102-522
# Assignment: Lab12 Act1
# Date: 13 November 2019

import matplotlib.pyplot as plt

def deriv(coeffs, exps):
    new_coeffs = []
    new_exps = []
    for i in range(len(coeffs)):
        new_coeffs.append(coeffs[i] * exps[i])
        new_exps.append(exps[i] - 1)
    return [new_coeffs, new_exps]

def f_of_x(x, coeffs, exps):
    y_val = 0
    for i in range(len(coeffs)):
        if coeffs[i] != 0 and x != 0:
            y_val += coeffs[i] * x**exps[i]
        if x == 0 and exps[i] == 0:
            y_val += coeffs[i]
    return y_val

coefficients_input = input("Please enter the coefficents of a function, separated by commas: ")
exponents_input = input("Please enter the exponents of the function (same number of terms), separated by commas: ")
interval_input = input("Please enter an interval on which to graph the function (2 terms): ")

coefficients = [float(i) for i in coefficients_input.split(",")]
exponents = [float(i) for i in exponents_input.split(",")]
interval = [float(i) for i in interval_input.split(",")]

num_of_x_vals = 100
interval_length = interval[1] - interval[0]
dx = interval_length / num_of_x_vals
x_vals = [i * dx + interval[0] for i in range(num_of_x_vals)]

# original function
y_vals = [f_of_x(i, coefficients, exponents) for i in x_vals]
plt.plot(x_vals, y_vals, "r-", label="Original function")

# first derivative
new_vals = deriv(coefficients, exponents)
coefficients = new_vals[0]
exponents = new_vals[1]
y_vals = [f_of_x(i, coefficients, exponents) for i in x_vals]
plt.plot(x_vals, y_vals, "b-", label="First derivative")

# second derivative
new_vals = deriv(coefficients, exponents)
coefficients = new_vals[0]
exponents = new_vals[1]
y_vals = [f_of_x(i, coefficients, exponents) for i in x_vals]
plt.plot(x_vals, y_vals, "g-", label="Second derivative")

plt.legend()
plt.title("Graph of the inputted function and its first and\nsecond derivatives on the inputted interval.")
plt.xlabel("x")
plt.ylabel("f")
plt.show()
