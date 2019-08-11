class Order:
    def __init__(self, description, quantity, price):
        self.description = description
        self.quantity = quantity
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price > 0.0:
            self.__price = price
        else:
            raise ValueError('Price should be bigger than 0')

    def subtotal(self):
        return self.quantity * self.price


if __name__ == "__main__":
    ord = Order('Ticket', 2, 100.0)
    print(ord.subtotal())
    ord.price = -100.0
