# By submitting this assignment, all team members agree to the following:
# # “Aggies do not lie, cheat, or steal, or tolerate those who do”
# # “I have not given or received any unauthorized aid on this assignment”
# #
# # Names: Josh Wood
# # Justin Compton
# # Braden Alexander
# # Troy Hays
# # Course/Section: ENGR 102-522
# # Assignment: Lab10 Act1
# Date: 28 October 2019

import numpy as np

# C) 1
print("c) 1. As a team, we have gone through all required sections of the tutorial,"
      "      and each team member understands the material.\n")

# C) 2
print("c) 2. ")
A = np.arange(12).reshape(3,4)
B = np.arange(8).reshape(4,2)
C = np.arange(6).reshape(2,3)
D = np.arange(3).reshape(3,1)
print("Matrix A:\n", A)
print("\nMatrix B:\n", B)
print("\nMatrix C:\n", C)
print("\nMatrix D:\n", D)

# C) 3
print("\nc) 3. ")
E = A@B@C
print("Matrix E:\n", E)

# C) 4
print("\nc) 4. ")
F = E.transpose()
print("Transpose of E:\n", F)

# C) 5
print("\nc) 5. ")
x = np.linalg.solve(E, D)
print("Solving for x in E*x = D: x =\n", x)
