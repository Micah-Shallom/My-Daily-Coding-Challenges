class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self,radius) -> None:
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    
class Rectangle(Shape):
    def __init__(self,width,height) -> None:
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    


c = Circle(5)
r = Rectangle(2,6)

for inst in (c,r):
    print(inst.area())