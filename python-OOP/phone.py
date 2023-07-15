from items import Item

class Phone(Item):
    #note that we also have access to all=[] from the parent class 
    def __init__(self, name: str, price: float, quantity, broken_phones):
        self.broken_phones = broken_phones
        super().__init__(
            name, price, quantity
        )

        assert broken_phones >= 0, f"Broken phones {broken_phones} is not given"
    
# phone1 = Phone("nokia", 5000, 3, 2)
# print(phone1.__dict__)
# print(phone1.calculate_total_quantity())
