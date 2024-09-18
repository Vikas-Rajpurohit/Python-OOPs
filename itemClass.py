class Item:

    # Instance Level then it goes to Class Level
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity = 0):
        # Run Validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        # Assign to self objects
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    # Functions inside class are called methods
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    # For representation of instances
    def __repr__(self):
        return f"Item({self.name}', {self.price}, {self.quantity})"


item1 = Item("Aditya", 5000, 1)
# print(item1.calculate_total_price())

# print(Item.__dict__)
# print(item1.__dict__)

item1.apply_discount()
# print(item1.price)

item2 = Item("Harsh", 1000, 1)
item2.pay_rate = 0.9
# Now has we set pay_rate at instance level it will update the value
item2.apply_discount()
# print(item2.price)

print(Item.all)
    