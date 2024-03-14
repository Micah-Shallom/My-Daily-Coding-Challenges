# interative method for solving a factorial problem
# e.g 4! = 4*3*2*1

def factorial(n):
    i = 1
    ans = 0
    while i < n:
        ans += n*(n-1)
        i += 1
    return ans
# print(factorial(4))

# Steps for solving a recursion problem
# Step1 - Recursive Case - the flow
# Step 2 - Base Case - set stopping condition/criterion
# Step 3 - Unintentional Case - the constraint 

import sys
sys.setrecursionlimit = "2000"

def Rfactorial(n):
    assert n >= 0 and int(n) == n, "The number must be positive integers only"

    if n in [0,1]:
        return 1
    return n * Rfactorial(n-1)

print(Rfactorial(1000))