# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Josh Wood
# Justin Compton
# Braden Alexander
# Troy Hays
# Course/Section: ENGR 102-522
# Assignment: Lab 13 Act1
# Date: 20 November 2019

from math import *
from matplotlib.pyplot import *

Vi = 10  # V
Vf = 25  # V
R = 30  # Ohm
L = 25  # mH
C = 60  # nF
a = R / (2 * L)
w0 = 1 / (L * C)
wd = sqrt(a**2 - w0**2)
delta_t = 10  # ms
t = []
vc = []

t += [i * 0.1 for i in range(8)]
vc += [(Vi - Vf) * exp(-a * i) * (cos(wd * i) + (a / wd) * sin(wd * i)) + Vf for i in t]  # 1st error
print(t)

print('Time'.ljust(10), 'Voltage across Capacitor'.ljust(25), end="")
print("")
print('__________'.ljust(10), '_______________'.ljust(25), end="")
print("")
for i in range(len(t)):
    print(str(round(t[i], 2)).ljust(10), str(round(vc[i], 3)).ljust(25))  # 2nd and 3rd error

i = 1
t += [i * delta_t]
vc += [(Vi - Vf) * (exp(-a * i)) * (cos(wd * i) + (a / wd) * sin(wd * i)) + Vf]

print(str(round(t[i], 1)).ljust(10), str(round(vc[i], 2)).ljust(25))

delta_vc = vc[i] - vc[i-1]
while delta_vc < 1e-4:
    i += 1
    t += [i * delta_t]
    vc += [(Vi - Vf) * (exp(-a * i)) * (cos(wd * i) + (a / wd) * sin(wd * i)) + Vf]
    print(str(round(t[i], 1)).ljust(10), str(round(vc[i], 2)).ljust(25))

plot(t, vc)
xlabel('t (ms)')
ylabel('vc (V)')
savefig("plot.jpg")
show()
