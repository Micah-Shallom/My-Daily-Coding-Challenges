# Write a Python program to calculate the sum of a list of numbers.

# def sumOfDigits(n):
#     if n < 10:
#         return n
#     else:
#         return n % 10 + sumOfDigits(n // 10) 

# print(sumOfDigits(25986))

def listOfDigits(n):
    if len(n) == 1:
        return n
    else:
        return n[0] + n[1:]


print(listOfDigits([2,3,4,5,6]))