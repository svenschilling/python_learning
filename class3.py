import csv

class Item:
    
    # discount of 20%
    pay_rate = 0.8 

    # all created instances 
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

    # @classmethod to make the function only useable on classlevel instead of both (class/instancetiate level)
    @classmethod
    def instantiateFromCSV(cls):
        # 'with' statement is like 'usign' in c# and get closed automaticly after use
        with open('item.csv','r') as csvFile:
            reader = csv.DictReader(csvFile)
            items = list(reader)
        
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    # representation of an object
    def __repr__(self):
        return f"obj repr = {self.itemName} , {self.itemPrice} : {self.itemQuantity}"


Item.instantiateFromCSV()
print(Item.all)
