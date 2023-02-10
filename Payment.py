class ToPayItem:

    def __init__(self, id, explain, price, pay_to):
        self.id = id
        self.explain = explain
        self.price = price
        self.pay_to = pay_to

class BoughtItem:

    def __init__(self, id, explain, price, owner):
        self.id = id
        self.explain = explain
        self.price = price
        self.owner = owner

class Debt:
    def __init__(self, name, amount):
        self.name = name
        self.price = amount