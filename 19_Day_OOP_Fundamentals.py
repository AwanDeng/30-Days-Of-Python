# Day 19 - Learning the basics of classes and objects

# Defining a custom class (blueprint)
class Car:
    pass

# Instantiating (creating) objects from the class
car1 = Car()
car2 = Car()

# Adding simple attributes to objects directly
car1.brand = "Toyota"
car1.color = "Red"

car2.brand = "Honda"
car2.color = "Blue"

print("Car 1 Brand:", car1.brand)
print("Car 1 Color:", car1.color)
print("Car 2 Brand:", car2.brand)