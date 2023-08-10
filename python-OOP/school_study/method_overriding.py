class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

# Creating instances
circle = Circle(5)

# Using the overridden method
print("Circle Area:", circle.area())  # Outputs: Circle Area: 78.5
