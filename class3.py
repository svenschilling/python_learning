class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # validations to received args
        assert price >= 0
        assert quantity >= 0 
        
        # assign to self object
        self.itemName = name
        self.itemPrice = price
        self.itemQuantity = quantity
        

        
    def calculatePrice(self):
        return self.itemPrice * self.itemQuantity

item1 = Item("Phone",100,5)
item2 = Item("Laptop",1000,3)
print(f"{item2.itemName} costs {item2.itemPrice}")


