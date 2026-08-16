# Day 18 - Preventing program crashes with try/except

# Trying to divide by zero
try:
    number = 10
    divider = 0
    result = number / divider
    print("Result:", result)
except ZeroDivisionError:
    print("Oops! You cannot divide a number by zero.")

print("Program continues safely without crashing!")