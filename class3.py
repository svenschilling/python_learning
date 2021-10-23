class Item:
    
    pay_rate = 0.8 # discount of 20%

    def __init__(self, name: str, price: float, quantity=0):
        # validations to received args
        assert price >= 0, f"Price {price} is not greater than or equal ro zero!"
        assert quantity >= 0, f"Price {quantity} is not greater than or equal to zero!"
        
        # assign to self object
        self.itemName = name
        self.itemPrice = price
        self.itemQuantity = quantity
        

        
    def calculatePrice(self):
        return self.itemPrice * self.itemQuantity

item1 = Item("Phone",100,5)
item2 = Item("Laptop",1000,3)
print(f"{item2.itemName} costs {item2.itemPrice}")

print(Item.__dict__)
print(item1.__dict__)