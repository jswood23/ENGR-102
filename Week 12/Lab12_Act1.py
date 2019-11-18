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

import matplotlib.pyplot as plt     # Imports matplotlib graphing module


def deriv(coeffs, exps):    # Declares function deriv with parameters "coeffs" and "exps"
    new_coeffs = []     # Creates empty list to store new coefficients
    new_exps = []       # Creates empty list to store new exponents
    for i in range(len(coeffs)):    # For loop to append each value to its corresponding list
        # Derivative of ax^n is anx^(n-1)
        new_coeffs.append(coeffs[i] * exps[i])
        new_exps.append(exps[i] - 1)
    return [new_coeffs, new_exps]   # Returns the two values as a list of the function


def f_of_x(x, coeffs, exps):    # Defines the function f of x with parameters "x", "coeffs", and "exps"
    y_val = 0
    for i in range(len(coeffs)):    # For loop calculates the equation
        if coeffs[i] != 0 and x != 0:    # For all non-zero exponents and values of x
            y_val += coeffs[i] * x**exps[i]
        if x == 0 and exps[i] == 0:    # If x=0 and the exponent is 0, 0^0 = 1 and y_val adds the term's coefficient
            y_val += coeffs[i]
    return y_val    # Returns y value of the function


# Asks the user for various input values
coefficients_input = input("Please enter the coefficients of a function, separated by commas: ")
exponents_input = input("Please enter the exponents of the function (same number of terms), separated by commas: ")
interval_input = input("Please enter an interval on which to graph the function (2 terms), separated by commas: ")

# Splits each variable by "," and appends that to the list
coefficients = [float(i) for i in coefficients_input.split(",")]
exponents = [float(i) for i in exponents_input.split(",")]
interval = [float(i) for i in interval_input.split(",")]

num_of_x_vals = 100  # Sets number of x-values to 100
interval_length = interval[1] - interval[0]  # Calculates the interval length
dx = interval_length / num_of_x_vals
x_vals = [i * dx + interval[0] for i in range(num_of_x_vals)]  # Calculates the x values

# original function
y_vals = [f_of_x(i, coefficients, exponents) for i in x_vals]   # Inserts parameters into the function f_of_x
plt.plot(x_vals, y_vals, "r-", label="Original function")   # Plots the graph, labeled "Original function"

# first derivative
new_vals = deriv(coefficients, exponents)  # Return list of two lists for values
coefficients = new_vals[0]  # Assign coefficient list to new variable
exponents = new_vals[1]  # Assign exponents list to new variable
y_vals = [f_of_x(i, coefficients, exponents) for i in x_vals]  # Compute y-values
plt.plot(x_vals, y_vals, "b-", label="First derivative")  # Add to final plot

# second derivative
new_vals = deriv(coefficients, exponents)    # Return list of two lists for values
coefficients = new_vals[0]  # Assign coefficient list to new variable
exponents = new_vals[1]  # Assign exponents list to new variable
y_vals = [f_of_x(i, coefficients, exponents) for i in x_vals]  # Compute y-values
plt.plot(x_vals, y_vals, "g-", label="Second derivative")  # Add to final plot

# Creates legend, labels, and title for graph
plt.legend()
plt.title("Graph of the inputted function and its first and\nsecond derivatives on the inputted interval")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()
