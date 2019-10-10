# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this
# assignment”
#
#  Names: Justin Compton
#  Braden Alexander
#  Josh Wood
#  Troy Hays
# Course/Section: ENGR 102-216
# Assignment: Lab 7, Activity 2
# Date: 9 October 2019

from math import *

# Part A
# A list of the grades given to us by professor
gradeData = [79, 99, 73, 49, 67, 62, 52, 99, 57, 58, 67, 88, 71, 69, 41, 74, 53, 90, 63,
             66, 92, 54, 61, 59, 48, 71, 83, 89, 99, 69, 66, 40, 48, 41, 99, 68, 52, 78, 77,
             71, 40, 65, 77, 87, 96, 44, 54, 60, 89, 72]

# Calculates the average grade among all the grades in the list
gradeMean = sum(gradeData) / len(gradeData)  # Average: sum of the grades divided by number of grades in the list

# Prints the average grade to the user
print('Part A\nAverage grade:', gradeMean, '\n')

# Part B
# Creates an empty list to store the values of the formula (n - mean)^2
diffSquare = []

# For loop subtracts the average grade from each number, squares that value, and stores it in a list
for i in gradeData:
    diffSquare.append(pow(i - gradeMean, 2))

# Calculates the average of the squared difference values
diffSquareMean = sum(diffSquare) / len(gradeData)

# Calculates the final step of the standard deviation equation
stdDev = sqrt(diffSquareMean)

# Prints the standard deviation of the grades to the user
print('Part B\nStandard deviation of the grades:', round(stdDev, 2))

# Part C

minGrade = gradeData[0]
maxGrade = gradeData[0]

for number in gradeData:
    if number < minGrade:
        minGrade = number
    elif number > maxGrade:
        maxGrade = number

print('\nPart C\nHighest grade:', maxGrade, '\nLowest grade:', minGrade)


# Part D
# newAvg = 75
# deltaGrade = newAvg / len(gradeData)
#
# newGradeData = [i + deltaGrade for i in gradeData]
#
# mean = sum(newGradeData) / len(newGradeData)
#
#
# print('\nPart D\nTo have a new class average of ' + str(newAvg) + ',', deltaGrade, 'points would need to be added '
#                                                                                    'to each person\'s test.')
# print(mean)

# deltaGrade = newAvg + ((newAvg-gradeMean) / (50 - min(gradeData) * (newAvg - gradeMean)))

# Part E
