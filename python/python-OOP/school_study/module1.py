"""
❑ Explain the following;
✓ Static Polymorphism - 
✓ Dynamic Polymorphism






❑ With the aid of an example, explain the following concepts of OOP;
✓ Encapsulation
✓ Abstraction
✓ Inheritance
✓ Polymorphism
❑ A program is to be written OO paradigm to calculate the diameter, radius and area of a circle
using only the encapsulation principle. List the members of the class? Which of members are
properties. Which members are methods?
❑ Write a python program to explain encapsulation?
❑ Differentiate between a subclass and superclass? Outline 2 uses of superclass?
❑ Differentiate between inheritance and overridden?
❑ Suppose that a class Employee is derived from a class Person. Give examples of data
variables and functions that can be added to the class employee?
"""

"""
Static polymorphism, also known as compile-time polymorphism, occurs when the decision about which method to call is made at compile time based on the method signature.

Dynamic polymorphism, also known as runtime polymorphism, occurs when the decision about which method to call is made at runtime based on the actual type of the object.


Superclass:

A superclass (also known as a base class or parent class) is a class that is extended or inherited by one or more other classes. It serves as a template for creating subclasses.
A superclass contains attributes, methods, and behaviors that are common to multiple subclasses.

Subclass:

A subclass (also known as a derived class or child class) is a class that inherits attributes and behaviors from a superclass.
A subclass can extend, specialize, or modify the attributes and methods inherited from the superclass.


Inheritance:

Inheritance is a mechanism in OOP that allows a new class (subclass or derived class) to inherit attributes and methods from an existing class (superclass or base class).

Method Overriding:

Method overriding occurs when a subclass provides its own implementation for a method that is already defined in its superclass.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department
        self.salary = 0

    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}, Department: {self.department}")
    
    def set_salary(self, salary):
        self.salary = salary
    
    def get_salary(self):
        return self.salary

# Creating instances
employee = Employee("John Doe", 30, "E12345", "Engineering")
employee.set_salary(60000)

# Using methods and attributes from both Person and Employee classes
employee.display_info()          # Outputs: Name: John Doe, Age: 30
employee.display_employee_info() # Outputs: Employee ID: E12345, Department: Engineering
print("Salary:", employee.get_salary())  # Outputs: Salary: 60000
