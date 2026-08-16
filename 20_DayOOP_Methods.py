# Day 20 - Learning constructors and methods

class Student:
    # Constructor method to initialize attributes
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    # Custom instance method
    def introduce(self):
        print("Hello, my name is " + self.name + " and I study " + self.course + ".")

    def is_adult(self):
        return self.age >= 18

# Creating student objects
student1 = Student("Alex", 20, "Computer Science")
student2 = Student("Sarah", 17, "Data Analytics")