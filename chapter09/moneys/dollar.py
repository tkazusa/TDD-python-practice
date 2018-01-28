from .money import Money

class Dollar(Money):
    """ dollar class"""

    def __init__(self):
        super(Dollar, self).__init__(amount, currency)


    def times(self, multiplier: int):
        return Dollar(self._amount * multiplier)

