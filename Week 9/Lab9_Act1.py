# For team submissions:
# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: NAME OF TEAM MEMBER 1
# NAME OF TEAM MEMBER 2
# NAME OF TEAM MEMBER 3
# NAME OF TEAM MEMBER 4
# Course/Section: ENGR 102-216
# Assignment: THE ASSIGNMENT NUMBER
# Date: DAY MONTH YEAR

inp = open('Celsius.dat', 'r')
out = open("Fahrenheit.dat", 'w')
x = inp.read()

for i in x.split('\n'):
    if i.isnumeric():
        f = (float(i) * 9 / 5) + 32
        out.write(str(f) + '\n')

inp.close()
out.close()

