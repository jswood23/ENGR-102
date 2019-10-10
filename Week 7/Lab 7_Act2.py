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
minGrade = gradeData[0]  # Creates an empty variable for the minimum score
maxGrade = gradeData[0]  # Create an empty variable for the maximum score

for number in gradeData:  # For loop compares each item in gradeData to the variables
    if number < minGrade:  # If the number is less than the minimum grade, that number is the new lowest grade
        minGrade = number
    elif number > maxGrade:  # If the number is greater than the maximum grade, that number is the new highest grade
        maxGrade = number

# Prints the highest and lowest grade to the user
print('\nPart C\nHighest grade:', maxGrade, '\nLowest grade:', minGrade)

# Part D
newAvg = 75  # Creates a variable for the teacher's new desired class average
sumNewAvg = newAvg * len(gradeData)     # Creates variable for the sum of the new average
sumGradeData = gradeMean * len(gradeData)   # Creates variable for the sum of the gradeData list

deltaGrade = int(sumNewAvg - sumGradeData) / len(gradeData)  # Calculates the delta grade

# Prints the value of the delta grade to the user
print('\nPart D\nIn order to have a new class average of ' + str(newAvg) + ', ' + str(deltaGrade) + ' points will need '
                                                                                                    'to be added to '
                                                                                                    'everybody\'s '
                                                                                                    'test.')

# Part E
median = 0  # Instantiates empty variable to hold the median test score
keep_going = False  # Conditional variable to control the while loop

# While loop checks if the list is even or odd
while not keep_going:
    if len(gradeData) % 2 == 0:     # If the list is even, the median is calculated accordingly
        gradeData.sort()
        length = len(gradeData)
        middle = len(gradeData) - 1
        median = ((gradeData[int(length / 2)] + gradeData[int(middle / 2)]) / 2.0)
        break

    elif len(gradeData) % 2 != 0:       # If the list is odd, the median is calculated accordingly
        gradeData.sort()
        length = len(gradeData)
        middle = len(gradeData) - 1
        median = ((gradeData[int(length / 2)] + gradeData[int(middle / 2)]) / 2.0)
        break

# The median test score is printed to the user
print('\nPart E\nMedian test score:', median)
