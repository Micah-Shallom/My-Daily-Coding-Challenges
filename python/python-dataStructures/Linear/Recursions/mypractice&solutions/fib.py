#  Write a Python program to solve the Fibonacci sequence using recursion.

def fibonnaci(n):
    if n in [0,1]:
        return n
    return fibonnaci(n-1) + fibonnaci(n-2)

print(fibonnaci(5))
