# Day 21 - List and Dictionary Comprehensions

# 1. List Comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Getting even numbers
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_numbers)

# Squaring numbers
squares = [x * x for x in numbers]
print("Squared numbers:", squares)

# 2. Dictionary Comprehension
names = ["Alex", "Sarah", "David"]

# Creating a dictionary of name lengths
name_lengths = {name: len(name) for name in names}
print("Name lengths dictionary:", name_lengths)