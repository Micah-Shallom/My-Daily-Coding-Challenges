import csv
class Item:
    payrate = 0.8
    all = []

    def __init__(self, name: str , price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        # Assign to self object
        self.__name = name
        self.__price = price 
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    # this ensure that the name attribute of the instance is read-only
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    
    def apply_discount(self):
        return self.__price * self.payrate
    
    def apply_increment(self,increment):
        self.__price += self.__price * increment
    
    
    @name.setter
    def name(self,value):
        if len(value) > 10:
            raise Exception("The name is too long")
        else:
            self.__name = value

     
    def calculate_total_quantity(self):
        return self.__price * self.quantity
    
    def apply_discount(self):
        # self.__price = self.__price * Item.payrate #the use of Item.payrate will always cause the class to pull the classbound payrate

        self.__price = self.__price * self.payrate #this will allow one to pull instance bound attributes
        return self.__price
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"
    
    @staticmethod
    def is_numeric(num):
        pass
    
    
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

    ##Understading the concepts of abstract
    def __connect(self,smtp_server):
        pass
    def __mail_body(self):
        pass
    def __delivery_status(self):
        pass

    #we abstract the above chaging them to private methods so that they cannot be instantiated directly from the instance but can only be put into use only by calling the send_email() method
    def send_email(self):
        self.__connect("")
        self.__mail_body()
        self.__delivery_status()