# def countdown(n):
#     while n > 0:
#         yield n
#         n -= 1

# # Using the generator function
# counter = countdown(5)
# for num in counter:
#     print(num)  # Output: 5, 4, 3, 2, 1



# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b

# # Using the generator function
# fib = fibonacci()
# for i in range(10):
#     print(next(fib))  # Output: Fibonacci sequence values

# # List comprehension with a generator function
# squares = (x**2 for x in range(10))
# print(list(squares))  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
