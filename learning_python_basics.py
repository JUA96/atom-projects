

# We need to import the necessary packages write code in python:

# numpy library allows us to do basic statistical analyzes
import numpy as np
# pandas enables us to load in data
import pandas as pd

import statistics as stats

# Mean and Median using stats package
mylist = [1, 12, 15, 19, 20]

print(np.mean(mylist))
print(stats.mean(mylist))

print(np.median(mylist))
print(stats.median(mylist))

# 2.1 The simple if statement
# The simplest example of a control structure is the if statement.

if 1 == 1:
    print('The integer 1 is equal to the integer 1.')
    print('Is the next indented line run, too?')

if 'one' == 'two':  # this evaluates as false
    print("The string 'one' is equal to the string 'two'.")

print('------')
print('These two lines are not indented, so they are always run next.')

# if...else statements
# In many cases, you may want to run some code if the expression evaluates to true and some different code if it evaluates to False. This is done using else. note how it is at the same indentation level as the if statement, followed by a colon, followed by a code block. Let's see it in action.

if 60 < 30:
    print("60 < 30.")
else:
    print("60 >= 30.")
    print("The else code block was run instead of the first block.")

print('---')
print('These two lines are not indented, so they are always run next.')

# if ... elif ... else statements
# Sometimes, you might want to run one specific code block out of several. For example, perhaps we provide the user with three choices and want something different to happen with each one.

# elif stands for else if. It belongs on a line between the initial if statement and an (optional) else.

health = 23

if health > 70:
    print('You are in great health!')
if health > 40:
    print('Your health is average.')
    print('Exercise and eat healthily!')
else:
    print('Your health is low.')
    print('See a doctor now.')

print('---')
print('These two lines are not indented, so they are always run next.')


# for Loops

for element in (range(50)):
    print(element+1)


for word in ["mary", "had", "a", "little", "lamb"]:
    print(word)


names = ['Paul', 'Nathalie', 'Catherine']
for name in names:
    print(name + ' Is Awesome!')


total = 0
for num in [0, 1, 2, 3, 4, 5]:
    total += num

print(total)


primes = [2, 3, 5]
for prime_number in primes:
    print(prime_number)

print('Done!')

# Changing a for loop:
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, area in enumerate(areas):
    print("room " + str(index) + ": " + str(area))


# while Loops

x = 0
while x < 10:
    x = x+1
    print(x)


# Offset while loop:
# Initialize offset
offset = -8

# Code the while loop
while offset != 0:
    print("correcting...")
    if offset > 0:
        offset = offset - 1
    else:
        offset = offset + 1
    print(offset)

# 5. Functions
# Functions in programming are a lot like mathematical functions. They take one or more inputs, do something and then return one or more outputs.

# In Python, there are built in functions (like 'print') and library functions (like math.sqrt), but we can also write our own functions to perform more specialised tasks.

# A function has to be defined first, and then called. The syntax and structure to define a function must include:

# The def keyword, followed by the function’s name
# The arguments of the function are given between parentheses followed by a colon
# The function body, correctly indented
# Optionally, the return statement
# We can define a simple function to square a number as follows.


def square(x):
    return x**2


y = square(3)
y


# Call the function with parameters/input/argument of our choice
x = 2
y = square(x)
print(x, y)


def sixth_power(mynumber):
    print(mynumber**6)


sixth_power(2)


# Dictionaries:


# Dictionary of dictionaries
europe = {'spain': {'capital': 'madrid', 'population': 46.77},
          'france': {'capital': 'paris', 'population': 66.03},
          'germany': {'capital': 'berlin', 'population': 80.62},
          'norway': {'capital': 'oslo', 'population': 5.084}}

# Dictionary of dictionaries
europe = {'spain': {'capital': 'madrid', 'population': 46.77},
          'france': {'capital': 'paris', 'population': 66.03},
          'germany': {'capital': 'berlin', 'population': 80.62},
          'norway': {'capital': 'oslo', 'population': 5.084}}


# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data = {'capital': 'rome', 'population': 59.83}

# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
print(europe)
