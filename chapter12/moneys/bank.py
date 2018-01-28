from .expression import Expression
from .money import Money

class Bank(object):
    """Bank class: temporary implementation
    """
    def __init__(self):
        pass

    def reduce(self, expression, currency):
        return Money.dollar(10)
