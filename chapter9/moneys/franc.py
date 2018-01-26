from .money import Money

class Franc(Money):
    """ franc class"""

    def __init__(self):
        super(Dollar, self).__init__(amount: int, currency: str)

    def times(self, multiplier: int):
        return Franc(self._amount * multiplier)
