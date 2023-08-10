class MathOperations:
    def add(self, a, b=None):
        if b is None:
            return a
        return a + b

# Creating an instance
math_ops = MathOperations()

# Using the overloaded method
print(math_ops.add(5))       # Outputs: 5
print(math_ops.add(3, 7))    # Outputs: 10
