# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Justin Compton
# Braden Alexander
# Josh Wood
# Troy Hays
# Course/Section: ENGR 102-201/216/522
# Assignment: Lab 7 1
# Date: 7 October 2019

# Part 1: CHALLENGE ACTIVITY 7.6.1
stock_prices = input("Part 1 -\nPlease enter three or more stock prices separated by spaces: ").split()

for price in stock_prices:
    print('$', price)

# Part 2: EXAMPLE (See Figure 7.7.2 zyBook)
# User inputs string w/ numbers: '203 12 5 800 -10'
print("\n\nPart 2 -\nPlease enter a string with numbers seperated by spaces.")
user_input = input('Enter numbers: ')

tokens = user_input.split()  # Split into separate strings

# Convert strings to integers
nums = []
for token in tokens:
    nums.append(int(token))

# Print each position and number
print()  # Print a single newline
for index in range(len(nums)):
    value = nums[index]
    print('%d: %d' % (index, value))

# Determine maximum even number
max_num = None
for num in nums:
    if (max_num == None) and (num % 2 != 0):
        # First odd number found
        max_num = num
    elif (max_num != None) and (num > max_num) and (num % 2 != 0):
        # Larger odd number found
        max_num = num

# Print results
print('Max odd #:', max_num)

# Part 3: CHALLENGE ACTIVITY 7.7.3: Hourly temperature reporting
myTemps = [76, 80, 82, 103, 95]

seperator = input("\n\nPart 3 -\nPlease enter a two character separator such as '--' or '<>': ")
for temp in myTemps:
    if myTemps.index(temp) < (len(myTemps) - 1):
        print(temp, seperator, end=' ')
    else:
        print(temp)

# Part 4: "Fake Sort" Routine
