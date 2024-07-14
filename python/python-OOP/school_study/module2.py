# `
# ❑ Write an OO program in Python to find the cost of a rectangular plot of land in Zaria LGA?
# ❑ Write a Python program using OO paradigm to calculate the diameter and area of a circular
# part of a cone. Also, the OO program should be able to calculate the volume of the cone. Use
# 3 of the principles of OOP in writing you Python codes.
# ❑ Extend your solution in question 2 in a manner that allows you to calculate the volume of
# water in a bucket.
# ❑ Differentiate between class attribute and instance attribute?
# ❑ What is an instance method?
# ❑ Write Python codes to explain the various forms of inheritance in OOP?
# ❑ Mention 4 benefits of bundling a code into individual software objects?


"""
Class Attribute:

A class attribute is an attribute that is shared among all instances of a class.
It is defined within the class but outside of any methods using the class_name.attribute_name syntax.
Class attributes are the same for all instances of the class and are not specific to any particular instance.
They are often used to define constants or default values that apply to all instances of the class.

Instance Attribute:

An instance attribute is an attribute that belongs to a specific instance of a class.
It is defined within the class's methods, typically within the __init__() method, using the self.attribute_name syntax.
Instance attributes are specific to each individual instance of the class.
"""

import math

class Cone:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def calculate_diameter(self):
        return self.radius * 2

    def calculate_area(self):
        slant_height = math.sqrt(self.radius**2 + self.height**2)
        lateral_area = math.pi * self.radius * slant_height
        base_area = math.pi * self.radius**2
        total_area = lateral_area + base_area
        return total_area

    def calculate_volume(self):
        return (1/3) * math.pi * self.radius**2 * self.height

class Bucket(Cone):
    def __init__(self, radius, height, water_level):
        super().__init__(radius, height)
        self.water_level = water_level

    def calculate_water_volume(self):
        cone_volume = self.calculate_volume()
        water_volume = cone_volume * (self.water_level / self.height)
        return water_volume

# Creating an instance of Cone
cone = Cone(5, 10)

# Calculating and printing diameter, area, and volume of the cone
print("Diameter:", cone.calculate_diameter())
print("Total Area:", cone.calculate_area())
print("Volume:", cone.calculate_volume())

# Creating an instance of Bucket
bucket = Bucket(7, 14, 8)

# Calculating and printing volume of water in the bucket
print("Volume of Water in the Bucket:", bucket.calculate_water_volume())
