class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def info(self):
        print(
            f'Name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}\n')

    def total_price(self):
        return self.price * self.quantity


class Electronics(Product):
    def __init__(self, name, price, quantity, warranty_years):
        super().__init__(name, price, quantity)
        self.warranty_years = warranty_years

    def info(self):
        super().info()
        print(f'Warranty: {self.warranty_years}')


class Clothing(Product):
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self.size = size

    def info(self):
        super().info()
        print(f'Size: {self.size}')


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name):
        for item in self.items:
            if item.name == item_name.name:
                print(f'{item.name} already exits')
                return
        self.items.append(item_name)

    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                return
        print(f'Item: {item_name} not found in the card')

    def show_cart(self):
        for item in self.items:
            item.info()

    def checkout(self):
        total = 0
        for price in self.items:
            total += price.total_price()
        if total >= 8000:
            discountamount = total * (10/100)
            total_amount = total - discountamount
            print(f'Discount amount: {discountamount}')
            print(f'Total amount after: {total_amount}')
        else:
            print(f'Grand total: {total}')


phone = Electronics('samsung', 4000, 1, 5)
addias = Clothing('addidas', 4000, 1, 'large')
cart = Cart()
cart.add_item(phone)
cart.add_item(addias)
cart.show_cart()
cart.remove_item('samsung')
print(f'After removing samsung')
cart.show_cart()
print(f'Final')
cart.add_item(phone)
cart.checkout()
