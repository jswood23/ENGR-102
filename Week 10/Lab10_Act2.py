# For team submissions:
# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Josh Wood
# # Justin Compton
# # Braden Alexander
# # Troy Hays
# Course/Section: ENGR 102-216
# Assignment: Lab 10 Activity 2
# Date: 27 October 2019

import numpy
import matplotlib.pyplot as plt

# Part C-1 (Josh)

def y_of_x(f, x):
    # function that returns a y value given the f and x values
    y = x ** 2 / (4 * f)
    return y

x_values = numpy.linspace(-2, 2, 50)  # 1-dimensional list of values: serves as the x-axis

plt.plot(x_values, y_of_x(2, x_values), "r-", label="f = 2", linewidth=2.0)  # red line for f = 2
plt.plot(x_values, y_of_x(6, x_values), "b-", label="f = 6", linewidth=4.0)  # blue line for f = 6

plt.xlim(-2, 2)  # set the x bounds of the plot to [-2, 2]
plt.ylim(0, 0.5)  # set the y bounds of the plot to [0, 0.5]
plt.legend()  # show the legend matching the color of a line to the value of f
plt.title("Lab 10 Activity 2 Part C.1")  # show the title of the plot
plt.ylabel("y")  # label the y axis
plt.xlabel("x")  # label the x axis

plt.show()  # open a new window with the plot

# Part C-2 (Braden)


# Part C-3 (Troy)
import matplotlib.pyplot as plt
import numpy as np

# Sine graph
xaxis = np.arange(-6, 6.5, 0.1)  # Creates x-values for sine graph
sinyaxis = np.sin(xaxis)  # Creates y-values for sine graph

# Cosine graph
cosyaxis = np.cos(xaxis)  # Creates y-values for cosine graph

# Graphs sine and cosine
plt.plot(xaxis, sinyaxis, label='sin(x)')
plt.plot(xaxis, cosyaxis, label='cos(x)', color='red')

plt.legend(loc='lower left')    # Creates legend for graphs

# Creates labels for the graph
plt.title('Plot of cos(x) and sin(x)')
plt.xlabel('x values')
plt.ylabel('y values')
plt.show()
