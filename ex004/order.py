import model


class Order(model.Model):
    quantity = model.NumberType()  # it's a descriptor
    price = model.NumberType()  # it's a descriptor

    def __init__(self, description, quantity, price):
        self.description = description
        self.quantity = quantity
        self.price = price

    def subtotal(self):
        return self.quantity * self.price


if __name__ == "__main__":
    ord = Order('Ticket', 2, 100.0)
    print(ord.subtotal())
    ord.price = -100.0
