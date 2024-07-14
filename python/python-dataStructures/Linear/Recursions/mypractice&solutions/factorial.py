# Write a Python program to get the factorial of a non-negative integer.


########################## Non Recursive Solution ###########################################


def nfactorial(n):
    # tot = 1
    # for each in [i for i in range(n+1) if i != 0 ]:
    #     tot *= each
    # return tot

    # tot = 1
    # for i in range(1,n+1):
    #     tot *= (i)

    # return tot

    i = 0
    ans = 1
    while i < n:
        ans *= n-i
        i += 1
    return ans


########################## Recursive Solution ###########################################

def rfactorial(n):
    if n == 0:
        return 1
    return n * rfactorial(n-1)

print(nfactorial(3))
print(rfactorial(5))