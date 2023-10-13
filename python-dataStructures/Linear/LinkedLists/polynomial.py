class PolynomialTerm:
    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next = None

class Polynomial:
    def __init__(self):
        # Initialize an empty linked list for the polynomial.
        self.head = None

    def add_term(self, coefficient, exponent):
        new_term = PolynomialTerm(coefficient, exponent)
        if not self.head:
            # If the list is empty, set the new term as the head.
            self.head = new_term
        else:
            current = self.head
            prev = None
            while current and current.exponent > exponent:
                prev = current
                current = current.next

            if current and current.exponent == exponent:
                # If a term with the same exponent exists, add coefficients.
                current.coefficient += coefficient
            else:
                # Insert the new term in the appropriate position.
                if prev:
                    prev.next = new_term
                else:
                    self.head = new_term
                new_term.next = current

    def display(self):
        current = self.head
        while current:
            print(f"{current.coefficient}x^{current.exponent}", end=" ")
            current = current.next
            if current:
                print("+", end=" ")
        print()

# Example usage:
poly = Polynomial()
poly.add_term(3, 2)  # 3x^2
poly.add_term(-2, 1)  # -2x^1
poly.add_term(5, 0)  # 5x^0 (constant term)
poly.add_term(1, 3)  # 1x^3

poly.display()  # Output: 1x^3 + 3x^2 - 2x^1 + 5x^0
