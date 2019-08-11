class NumberType:
    def __init__(self):
        self.target = f'NumberType_{id(self)}'

    def __get__(self, instance, owner):
        return getattr(instance, self.target)

    def __set__(self, instance, value):
        if value > 0.0:
            setattr(instance, self.target, value)
        else:
            raise ValueError('Value should be bigger than 0')


class Order:
    quantity = NumberType()  # it's a descriptor
    price = NumberType()  # it's a descriptor

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
