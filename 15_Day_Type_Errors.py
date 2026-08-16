# Day 15 - Common beginner errors and how to spot them

# 1. TypeError example (cannot add string and number directly)
try:
    age = 20
    message = "My age is " + age  # This causes error
except TypeError:
    print("Caught TypeError: You must convert the number to a string using str()!")

# Fixed version:
print("My age is " + str(20))