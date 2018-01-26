from .money import Money

class Dollar(Money):
    """ dollar class"""

    def __init__(self, amount, currency):
        super(Dollar, self).__init__(amount, currency)

