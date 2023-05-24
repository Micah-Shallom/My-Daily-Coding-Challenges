def firstMethod():
    secondMethod()
    print("I am the first method")

def secondMethod():
    thirdMethod()
    print("I am the second method")

def thirdMethod():
    fourthMethod()
    print("I am the third method")

def fourthMethod():
    # firstMethod()
    print("I am the fourth method")

firstMethod()

# Another simple implementation of recursions

def recursionMethod(n):
    if n<1:
        print(f"{n} is less than 1")
    else:
        recursionMethod(n-1)
        print(n)

# recursionMethod(4) 


def powerOfTwoIT(n):
    i = 0
    power = 1
    while i < n:
        power *= 2
        i += 1
    print(power)

# powerOfTwoIT(5)

def powerOfTwoRM(n):
    if n == 0:
        return 1
    else:
        power = powerOfTwoRM(n-1)
        print(power)
        return power * 2 
# print(powerOfTwoRM(5))