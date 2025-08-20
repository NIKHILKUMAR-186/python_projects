inventory = {} # Example: {'Laptop': <Product object>}
class product():
    def __init__(self , name , price , quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        print(f"Name: {self.name}, Price: ${self.price}, Quantity: {self.quantity}")

    def add_product():
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        inventory[name] = product(name, price, quantity)
        print("Product added successfully!")
