class Item:
    def __init__(self,name,price,quantity):
        print(f"An Instance of {name} got created")
        self.itemName = name
        self.itemPrice = price
        self.itemQuantity = quantity        
        
    def calculatePrice(self):
        return item1.itemPrice * item1.itemQuantity

item1 = Item("Phone",100,5)
print(f"The Sum of {item1.itemName} costs {item1.calculatePrice()}")
