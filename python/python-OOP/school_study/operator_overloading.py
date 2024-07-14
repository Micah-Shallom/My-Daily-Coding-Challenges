# a,b = 5,6
# c,d = "a","b"
# print(a+b)
# print(int.__add__(a,b))
# print(str.__add__(c,d))

class Student:
    def __init__(self, m1, m2) -> None:
        self.m1 = m1
        self.m2 = m2

    def __add__(self,other):
        s1 = self.m1 + other.m1
        s2 = self.m2 + other.m2
        s3 = Student(s1, s2)
        return s3
    
    def __str__(self) -> str:
        return f"{self.m1} {self.m2}"



s1 = Student(1,2)
s2 = Student(3,4)
s3 = s1 + s2
print(s3)
print(Student.__add__(s1,s2))