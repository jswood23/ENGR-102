# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Josh Wood
# Justin Compton
# Braden Alexander
# Troy Hays
# Course/Section: ENGR 102-522
# Assignment: Lab9 Act2
# Date: 26 October 2019

# Introduction
import csv

print("Howdy!\nThis program calculates and saves to a file a list of amortized values for a loan")
print("Enter the amount of the loan, the annual interest rate, and the monthly payment amount below")

# Ask for amount of loan, annual interest rate, and monthly payment amount
loan = float(input("Amount of loan: "))
annual_interest_rate = float(input("Annual Interest Rate: "))
monthly_payment = float(input("Monthly Payment Amount: "))
beginning_balance = loan

# Ask for name of file and add '.csv' extension
print("\nNext, enter the name of the file to write the results to")
file_name = input("File Name: ").rstrip() + '.csv'

# Calculate Monthly Accrued interest
monthly_accrued_interest = (1/12) * beginning_balance * (annual_interest_rate / 100)  # First Month

# Principal payback amount = monthly payment amount - monthly accrued interest
principal_payback = monthly_payment - monthly_accrued_interest  # First Month

# Ending balance = beginning balance - principal payback amount
ending_balance = beginning_balance - principal_payback

# Open new file to write to for rest of values
with open(file_name, 'w', newline='') as csvfile:
    file_writer = csv.writer(csvfile)  # Use imported csv module

    header = ['Month', 'Beginning Balance', 'Monthly Accrued Interest',
              'Principal Payback Amount', 'Ending Balance', 'Total Interest Accrued']
    file_writer.writerow(header)

    month = [1, round(beginning_balance, 2), round(monthly_accrued_interest, 2),
             round(principal_payback, 2), round(ending_balance, 2), round(monthly_accrued_interest, 2)]
    file_writer.writerow(month)  # Write the first month's values to file

    if monthly_accrued_interest >= monthly_payment:  # If ending balance increases or stays the same
        interest_sum = monthly_accrued_interest  # Running total for interest
        for n in range(2, 31):  # Calculates and writes data for first 30 months
            beginning_balance = ending_balance
            monthly_accrued_interest = (1 / 12) * beginning_balance * (annual_interest_rate / 100)
            interest_sum += monthly_accrued_interest
            principal_payback = monthly_payment - monthly_accrued_interest
            ending_balance = beginning_balance - principal_payback
            month = [n, round(beginning_balance, 2), round(monthly_accrued_interest, 2),
                     round(principal_payback, 2), round(ending_balance, 2), round(interest_sum, 2)]
            file_writer.writerow(month)  # Write all months through loop

    else:  # If loan will be paid off
        interest_sum = monthly_accrued_interest  # Running total for interest
        n = 2  # Counter for months
        while ending_balance > 0:  # Calculates and writes data until loan is paid off
            beginning_balance = ending_balance
            monthly_accrued_interest = (1 / 12) * beginning_balance * (annual_interest_rate / 100)
            interest_sum += monthly_accrued_interest
            principal_payback = monthly_payment - monthly_accrued_interest
            ending_balance = beginning_balance - principal_payback
            month = [n, round(beginning_balance, 2), round(monthly_accrued_interest, 2),
                     round(principal_payback, 2), round(ending_balance, 2), round(interest_sum, 2)]
            file_writer.writerow(month)  # Write all months through loop
            n += 1  # Keeps track of number of months
