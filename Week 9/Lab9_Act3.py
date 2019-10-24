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

file = open('WeatherDataWindows.csv', 'r')
s = file.readlines()
del s[:1]

weatherList = []
for item in s:
    weatherList.append(item.strip().split(','))

date = []
tempHigh = []
tempAvg = []
tempLow = []
dewPointHigh = []
dewPointAvg = []
dewPointLow = []
humidHigh = []
humidAvg = []
humidLow = []
pressureHigh = []
pressureAvg = []
pressureLow = []
precipitation = []
maxminTemp = []

for i in range(len(weatherList)):
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

maxTemp = 0

for item in tempHigh:
    item = float(item)
    if item > maxTemp:
        maxTemp = item

print('Part (a)\nThe maximum and minimum temperatures seen over the past 3 years are below.')
print('Date \t\t\tMaximum Temperature\t\t\tMinimum Temperature')

for item in date:
    print(item)
