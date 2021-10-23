class Item:
    
    pay_rate = 0.8 # discount of 20%

    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # validations to received args
        assert price >= 0, f"Price {price} is not greater than or equal ro zero!"
        assert quantity >= 0, f"Price {quantity} is not greater than or equal to zero!"
        
        # assign to self object
        self.itemName = name
        self.itemPrice = price
        self.itemQuantity = quantity

        # append all instances 
        Item.all.append(self)


    def calculatePrice(self):
        return self.itemPrice * self.itemQuantity

    def applyDiscount(self):
        self.itemPrice *= self.pay_rate

item1 = Item("Phone",100,5)
item2 = Item("Laptop",1000,3)
item3 = Item("Cable",10,5)
item4 = Item("Mouse",50,5)
item5 = Item("Keyboard",75,5)

print(f"{item2.itemName} costs {item2.itemPrice}")

print(Item.__dict__)
print(item1.__dict__)

item1.applyDiscount()
print(item1.itemPrice)

item2.pay_rate = 0.7
item2.applyDiscount()
print(item2.itemPrice)

print(Item.all)

for instance in Item.all:
    print(instance.itemName)