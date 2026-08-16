# Day 14 - Passing functions into other functions

numbers = [1, 2, 3, 4, 5, 6]

# Using map to double every number
def double(x):
    return x * 2

doubled_list = list(map(double, numbers))
print("Doubled numbers:", doubled_list)

# Using filter to keep only even numbers
def is_even(x):
    return x % 2 == 0

even_numbers = list(filter(is_even, numbers))
print("Even numbers only:", even_numbers)