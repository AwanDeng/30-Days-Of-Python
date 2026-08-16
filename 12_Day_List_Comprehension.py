# Day 12 - A shorter way to make lists

# The long beginner way:
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num * num)

print("Squared list (long way):", squared_numbers)

# The list comprehension way:
short_squared = [num * num for num in numbers]
print("Squared list (short way):", short_squared)