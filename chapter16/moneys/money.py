class Money(object):
    """Money class"""

    def __init__(self, amount: int, currency: str):
        self.amount = amount
        self._currency = currency

    def __eq__(self, other):
        return self.amount == other.amount and \
            self.currency() == other.currency()
    
    def __repr__(self):
        return str(self.amount) + " " + self._currency

    def times(self, multiplier: int):
        return Money(self.amount * multiplier, self.currency())

    def currency(self):
        return self._currency

    def plus(self, addend):
        from .sum import Summation
        return Summation(self, addend)
    
    def reduce(self, bank, currency):
        rate = 2 if (self.currency() == "CHF" and currency == "USD") else 1
        return Money(self.amount / rate, currency)

    @staticmethod
    def dollar(amount: int):
        """"create dollar"""
        return Money(amount, "USD")
    
    @staticmethod
    def franc(amount: int):
        """"create franc"""
        return Money(amount, "CHF")


