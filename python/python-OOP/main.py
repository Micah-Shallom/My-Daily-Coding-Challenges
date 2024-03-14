from items import Item
from phone import Phone


    
# Item.instantiate_from_csv()

item1 = Item("NewItem", 100000)
item1.name = "nameditem"
item1.apply_increment(0.2)
print(item1.price)
print(item1)

# print([each.name for each in Item.all])




