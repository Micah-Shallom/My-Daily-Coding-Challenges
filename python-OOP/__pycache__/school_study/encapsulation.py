#Example of a Public Member

class Car:
    def __init__(self,make,model) -> None:
        self.make = make
        self.model = model


    def start_engine(self):
        print(f"The {self.make} {self.model}'s engine has started")


my_car = Car("Toyota","Camry")

# Accessing and modifying public attributes directly
print(f"My car is a {my_car.make} {my_car.model}.")
my_car.model = "Corolla"
print(f"Now it's a {my_car.make} {my_car.model}.")

my_car.start_engine()


#Example of using a Protected Member

class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self._age = age

    def display_info(self):
        print(f"My name is {self.name} and i am {self._age} years old")


person = Person("Shallom",23)

print(person.name, person._age)
person.display_info()

#Example use of a Private member

class Bank:
    def __init__(self,amount, balance) -> None:
        self._amount = amount
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        if amount > self.__balance:
            return "Insufficient Balance"
        else:
            self.__balance -= amount

gtbank = Bank(230, 10000000000000)
