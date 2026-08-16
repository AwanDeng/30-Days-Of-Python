# Day 11 - Writing my own functions

# A simple function that says hello
def say_hello(name):
    print("Hello " + name + "! Welcome to Python.")

# Calling the function
say_hello("Alex")
say_hello("Sarah")

# A function that adds two numbers and returns the answer
def add_numbers(a, b):
    answer = a + b
    return answer

result = add_numbers(10, 20)
print("10 + 20 =", result)