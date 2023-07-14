import csv
class Item:
    payrate = 0.8
    all = []

    def __init__(self, name: str , price: float, quantity):
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        # Assign to self object
        self.name = name
        self.price = price 
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    
    def calculate_total_quantity(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        # self.price = self.price * Item.payrate #the use of Item.payrate will always cause the class to pull the classbound payrate

        self.price = self.price * self.payrate #this will allow one to pull instance bound attributes
        return self.price
    
    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    
    @classmethod
    def instantiate_from_csv(cls):
        with open("./items.csv", 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
    
Item.instantiate_from_csv()

# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

print(Item.all)
# print([each.name for each in Item.all])





# class MyClass:
#     class_variable = "my variable"

#     def __init__(self,instance_variable) -> None:
#         self.instance_variable = instance_variable

#     @classmethod
#     def classmethod(cls):
#         return cls.class_variable
    
#     def instancemethod(self):
#         return self.instance_variable
    

# print(MyClass.classmethod())
# mclass = MyClass("Shallom class variable")
# print(mclass.instancemethod())