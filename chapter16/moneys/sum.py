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

    def reduce(self, bank, currency):
        amount = self.augend().reduce(bank, currency).amount + \
            self.addend().reduce(bank, currency).amount
        return Money(amount, currency)

    def plus(self, addend):
        return Summation(self, addend)

    def times(self, multiplier):
        return Summation(self.augend().times(multiplier), self.addend().times(multiplier))
