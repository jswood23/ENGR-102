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
Vi = 10 # V
Vf = 25 # V

# added lines:
Vi = float(input("Enter the initial voltage: "))
Vf = float(input("Enter the final voltage: "))

ti = 0.1e-3  # s
R = 300 # Ohm
L = 25e-3 # H
C = 60e-9 # F
a = R/(2*L)
w0 = 1/sqrt(L*C)
wd = sqrt(w0**2 - a**2)
delta_t = 0.005e-3  # s
t = []


t += [ti]
vc=[(Vi-Vf)*(exp(-a*t[0]))*(cos(wd*t[0]+(a/wd)*(sin(wd))*t[0]))+Vf]  # 1st error: vc not defined, used 'i' instead of '0'
print('Time'.ljust(20),'Voltage across Capacitor'.ljust(25),end="")
print("")
print('__________'.ljust(20), '_______________'.ljust(25), end="")
print("")
print((str(round(t[0] * 10**3,3)) + " milliseconds").ljust(20),(str(round(vc[0],2)) + " V").ljust(25))  # used [0] instead of [i], multiplied t by 1000
i = 1
t += [ti+i*delta_t]  # add values to ti
vc+=[(Vi-Vf)*(exp(-a*t[i]))*(cos(wd*t[i]+(a/wd)*(sin(wd))*t[i]))+Vf]
print((str(round(t[i] * 10**3,3)) + " milliseconds").ljust(20),(str(round(vc[i],2)) + " V").ljust(25))  # multiplied t by 1000
delta_vc = vc[i] - vc[i-1]
while delta_vc > 1e-4:  # delta_vc should be greater than 1e-4 at first, not less than

    i+=1  # add to i within the while loop
    t += [ti+i*delta_t]  # lines not indented, add values to ti
    vc+=[(Vi-Vf)*(exp(-a*t[i]))*(cos(wd*t[i]+(a/wd)*(sin(wd))*t[i]))+Vf]
    print((str(round(t[i] * 10**3, 3)) + " milliseconds").ljust(20), (str(round(vc[i], 2)) + " V").ljust(25))  # multiplied t by 1000
    delta_vc = vc[i] - vc[i-1]  # delta_vc did not change within the while loop

from matplotlib.pyplot import *
plot(t,vc)
xlabel('t (s)')
ylabel('vc (V)')
savefig("plot.jpg")
show()
