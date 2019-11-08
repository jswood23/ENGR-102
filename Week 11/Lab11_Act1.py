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

# Part a)

# Part b)

# Part c)
def newton_step(num):
    approximation = initial_guess - (F(num)/deriv(num))
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
F = eval(input("Enter a function in appropriate Python syntax: "))
x0 = float(input("Enter the initial guess for a root of the function: ")

print("Successive root approximations:\n", newton(x0))

# Part f)

# Part g)

# Challenge a)

# Challenge b)
