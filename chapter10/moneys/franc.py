from .money import Money

class Franc(Money):
    """ franc class"""

    def __init__(self, amount, currency):
        super(Franc, self).__init__(amount, "CHF")
