"""
>>> ord = Order('Ticket', 2, 100.0)
>>> ord.subtotal()
200.0

>>> ord.price = -100.
>>> ord.subtotal()
-200.0
"""


class Order:
    def __init__(self, description, quantity, price):
        self.description = description
        self.quantity = quantity
        self.price = price

    def subtotal(self):
        return self.quantity * self.price


if __name__ == "__main__":
    import doctest
    doctest.testmod()
