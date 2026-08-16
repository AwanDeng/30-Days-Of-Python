# Day 07 - Learning about Sets (no duplicate items allowed)

# Creating a set
numbers = {1, 2, 3, 4, 4, 5}  # Notice the extra 4
print("Set automatically removes duplicates:", numbers)

# Adding an item
numbers.add(6)
print("After adding 6:", numbers)

# Combining two sets
set_a = {1, 2, 3}
set_b = {3, 4, 5}
combined = set_a.union(set_b)
print("Combined set:", combined)