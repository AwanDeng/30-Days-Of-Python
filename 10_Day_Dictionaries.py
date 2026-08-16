# Day 10- Learning about dictionaries (key and value pairs)

# Creating a dictionary for a student
student = {
    "name": "Alex",
    "age": 20,
    "course": "Computer Science",
    "grade": "A"
}

# Accessing values using keys
print("Student name:", student["name"])
print("Student grade:", student["grade"])

# Adding a new key-value pair
student["city"] = "Nairobi"
print("Updated student info:", student)

# Updating an existing value
student["age"] = 21
print("New age:", student["age"])