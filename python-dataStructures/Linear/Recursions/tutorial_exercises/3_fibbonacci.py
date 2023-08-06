def fibonacci(n):
    assert n>=0 and int(n) == n, "Fibonacci number cannot be negative or non integer"
    if n in [0,1]:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(4)) 