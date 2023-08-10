# Write an OOP programs of your choice using the concepts:
# ✓ Dock typing
# ✓ 3 different operator overloading
# ✓ Method overriding
# ❑ How does polymorphism enable promote software extensibility?
# ❑ Differentiate between an abstract class and a concrete class
# ❑ What is an interface? Explain the concept of interfaces in OOP
# context?
# ❑ Differentiate between dynamic binding and static binding?
# ❑ Differentiate between the inheritance hierarchies designed for
# inheriting interface and the ones designed for inheriting
# implementations?

"""
Abstract Class:
An abstract class is a class that cannot be instantiated on its own; it serves as a blueprint for other classes.
It may have abstract methods (methods without implementations) that must be overridden by its subclasses.

Concrete Class:
A concrete class is a class that can be instantiated directly to create objects.
It can have both abstract and non-abstract methods, and it can provide implementations for all its methods.


Static Binding:

Static binding, also known as early binding, occurs at compile time.
It's used when the compiler can determine the method to be called based on the type of the variable at compile time.
Method overloading is an example of static binding.
Dynamic Binding:

Dynamic binding, also known as late binding or runtime binding, occurs at runtime.
It's used when the actual method to be called is determined based on the actual type of the object at runtime.
Method overriding is an example of dynamic binding.

Inheriting Interface:
In an inheritance hierarchy designed for inheriting interfaces, subclasses inherit only the method signatures (contract) defined in the interfaces.
Subclasses are required to provide their own implementations for the methods declared in the interfaces they implement.
Inheriting Implementations:
In an inheritance hierarchy designed for inheriting implementations, subclasses inherit both method signatures and the actual implementations of methods from a common superclass.
Subclasses can choose to override inherited methods or inherit their behavior as-is.
"""

class Duck:
    def quack(self):
        return "Quack!"
    
    def swim(self):
        return "Swimming"

class Robot:
    def quack(self):
        return "Beep boop!"
    
    def swim(self):
        return "Robots can't swim"
    
    def fly(self):
        return "Flying"

class Dog:
    def bark(self):
        return "Woof!"
    
    def swim(self):
        return "Dogs can swim"

def perform_duck_behavior(entity):
    print(entity.quack())
    print(entity.swim())

# Using Duck Typing
duck = Duck()
robot = Robot()
dog = Dog()

print("Duck Behavior:")
perform_duck_behavior(duck)

print("\nRobot Behavior:")
perform_duck_behavior(robot)

# Operator Overloading
class CustomNumber:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

# Using Operator Overloading
num1 = CustomNumber(10)
num2 = CustomNumber(5)

sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2

print("Sum:", sum_result)     # Outputs: Sum: 15
print("Difference:", diff_result)  # Outputs: Difference: 5
print("Product:", prod_result)     # Outputs: Product: 50


# Method Overriding
class Vehicle:
    def move(self):
        return "Moving forward"

class Car(Vehicle):
    def move(self):
        return "Driving on roads"

class Airplane(Vehicle):
    def move(self):
        return "Flying through the skies"

# Using Method Overriding
vehicle = Vehicle()
car = Car()
airplane = Airplane()

print("\nVehicle Movements:")
print("Vehicle:", vehicle.move())
print("Car:", car.move())
print("Airplane:", airplane.move())
