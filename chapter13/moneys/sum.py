from .money import Money
from .expression import Expression

class Summation(Expression):
    """summation of moneys
    """
    def __init__(self, augend, addend):
        self._augend = augend
        self._addend = addend

    def augend(self):
        return self._augend

    def addend(self):
        return self._addend

    def reduce(self, currency):
        amount = self.augend().amount + self.addend().amount
        return Money(amount, currency)

