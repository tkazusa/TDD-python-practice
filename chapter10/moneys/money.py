class Money(object):
    """Money class"""

    def __init__(self, amount: int, currency: str):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other):
        return self._amount == other._amount and \
            self.currency() == other.currency()
    
    def __repr__(self):
        return str(self._amount) + " " + self._currency

    def times(self, multiplier: int):
        return Money(self._amount * multiplier, self.currency())

    def currency(self):
        return self._currency

    @staticmethod
    def dollar(amount: int):
        """"create dollar"""
        from .dollar import Dollar
        return Dollar(amount, "USD")
    
    @staticmethod
    def franc(amount: int):
        """"create franc"""
        from .franc import Franc
        return Franc(amount, "CHF")

    
