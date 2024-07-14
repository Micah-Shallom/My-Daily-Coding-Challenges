class Student:
    def __init__(self,m1,m2) -> None:
        self.m1 = m1
        self.m2 = m2

    def __add__(self,other):
        x1 = self.m1 + other.m1
        x2 = self.m2 + other.m2
        c1 = self.m1 + self.m2
        c2 = other.m1 + other.m2
        x3 = x1 + x2
        return x3, x1, x2, c1, c2


s1 = Student(1,2)
s2 = Student(3,4)

print(s1+s2)