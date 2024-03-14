#Example usage of abstract classes and abstract methods

from abc import ABC, abstractmethod

#abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

#concrete class
class Area(Shape):
    def __init__(self,radius) -> None:
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
#concrete class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    
ar = Area(20)
print(ar.area())


# More complex example on the use of abstract classes and methods
class BankAccount(ABC):
    def __init__(self,account_number,balance,) -> None:
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def withdraw(self,amount):
        pass

    def get_balance(self):
        return self.balance
    

class SavingsAccount(BankAccount):
    def __init__(self,account_number,balance, interest_rate):
        super().__init__(account_number,balance)
        self.interest_rate = interest_rate

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Funds")

    def calculate_interest(self):
        return self.balance * self.interest_rate
    
class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
        else:
            print("Transaction declined due to insufficient funds.")
    
# Creating instances of the subclasses
savings_account = SavingsAccount("123456", 1000, 0.05)
checking_account = CheckingAccount("789012", 500, 100)

# Using the methods defined in the abstract class
savings_account.deposit(200)
checking_account.withdraw(700)

# Using the methods specific to each subclass
print(f"Savings Account Interest: ${savings_account.calculate_interest():.2f}")
print(f"Checking Account Balance: ${checking_account.get_balance()}")
 
