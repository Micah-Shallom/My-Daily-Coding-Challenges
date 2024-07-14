# Write a recursive function summation(n) that takes in a positive integer n, and returns the sum of numbers from 1 to n.

######################## Non Recursive Solution #########################################

def summation(n):
    return sum(i for i in range(n+1))


######################## Recursive Solution ##############################################

def summation(n):
    if n == 0:
        return 0
    else:
        return n + summation(n-1)



print(summation(1))  # 1
print(summation(2))  # 3
print(summation(3))  # 6
print(summation(4))  # 10
print(summation(5))  # 15
print(summation(6))  # 21
print(summation(7))  # 28
print(summation(8))  # 36