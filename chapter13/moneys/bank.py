from .expression import Expression
from .money import Money

class Bank(object):
    """Bank class: temporary implementation
    """
    def __init__(self):
        pass

    def reduce(self, source: Expression, currency):
        return source.reduce(currency)
