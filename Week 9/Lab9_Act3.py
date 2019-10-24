# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this
# assignment”
#
# Names: Justin Compton
# Braden Alexander
# Josh Wood
# Troy Hays
# Course/Section: ENGR 102-216
# Assignment: Lab 9, Activity 3
# Date: 23 October 2019

file = open('WeatherDataWindows.csv', 'r')  # Opens the weather data file
s = file.readlines()  # Reads the line of the file
del s[:1]  # Deletes the first row because it is just headers

weatherList = []  # Creates empty list to store all raw data
for item in s:
    weatherList.append(item.strip().split(','))  # Appends each item in the file to the list

# Creates an empty list to store each of the category data
date = []  # Stores all of the dates
tempHigh = []  # Stores all of the high temperatures
tempAvg = []  # Stores all of the average temperatures
tempLow = []  # Stores all of the low temperatures
dewPointHigh = []  # Stores all of the high dew point levels
dewPointAvg = []  # Stores all of the average dew point levels
dewPointLow = []  # Stores all of the low dew point levels
humidHigh = []  # Stores all of the high humidity levels
humidAvg = []  # Stores all of the average humidity levels
humidLow = []  # Stores all of the low humidity levels
pressureHigh = []  # Stores all of the high pressure levels
pressureAvg = []  # Stores all of the average pressure levels
pressureLow = []  # Stores all of the low pressure levels
precipitation = []  # Stores all of the precipitation
datemaxminTemp = []  # Stores the date, max temperature, and minimum temperature in a list for part A
dateavgPrecip = []  # Stores the date, and precipitation together in a list for part B

for i in range(len(weatherList)):  # Appends each item to it's corresponding list
    date.append(weatherList[i][0])
    tempHigh.append((weatherList[i][1]))
    tempAvg.append(weatherList[i][2])
    tempLow.append(weatherList[i][3])
    dewPointHigh.append(weatherList[i][4])
    dewPointAvg.append(weatherList[i][5])
    dewPointLow.append(weatherList[i][6])
    humidHigh.append(weatherList[i][7])
    humidAvg.append(weatherList[i][8])
    humidLow.append(weatherList[i][9])
    pressureHigh.append(weatherList[i][10])
    pressureAvg.append(weatherList[i][11])
    pressureLow.append(weatherList[i][12])
    precipitation.append(weatherList[i][13])

# Part A
print('\nPart (a)\nThe maximum and minimum temperatures seen over the past 3 years are below.')  # Prints intro
print('Date \t\t\t\t\t\t\t\t\tMaximum Temperature\t\tMinimum Temperature')  # Prints headers

for i in range(len(date)):  # Appends the date, the high temperature, and the low temperature to the datemaxminTemp list
    datemaxminTemp.append(date[i])
    datemaxminTemp.append(tempHigh[i])
    datemaxminTemp.append(tempLow[i])
    datemaxminTemp.append('\n')

print(*datemaxminTemp, sep='\t\t\t\t\t')  # Prints the result. THE FORMATTING NEEDS FIXING

# Part B
print('\nPart (b)The average daily precipitation seen over the 3 year period is below')
print('\t\t\tDate\t\t\t\tAverage Daily Precipitation')

for i in range(len(date)):  # Appends the date, and the precipitation to the dateavgPrecip list
    dateavgPrecip.append(date[i])
    dateavgPrecip.append(precipitation[i])
    dateavgPrecip.append('\n')

print(*dateavgPrecip, sep='\t\t\t') # Prints the result. THE FORMATTING NEEDS FIXING
