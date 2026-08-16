# Day 13 - Importing built-in Python modules

import math
import random

# Using the math module
print("Square root of 16 is:", math.sqrt(16))
print("Value of Pi:", math.pi)

# Using the random module
random_number = random.randint(1, 10)
print("Random number between 1 and 10:", random_number)

fruits = ["apple", "banana", "cherry"]
picked_fruit = random.choice(fruits)
print("Randomly picked fruit:", picked_fruit)