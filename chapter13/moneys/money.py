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

    def plus(self, added):
        return Money(self.amount + added.amount, self.currency())

    @staticmethod
    def dollar(amount: int):
        """"create dollar"""
        return Money(amount, "USD")
    
    @staticmethod
    def franc(amount: int):
        """"create franc"""
        return Money(amount, "CHF")

