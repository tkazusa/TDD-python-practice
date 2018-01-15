class Dollar(object):
    """ dollar class"""

    def __init__(self, amount: int):
        self._amount = amount

    def times(self, multiplier: int):
        return Dollar(self._amount * multiplier)

    def __eq__(self, other):
        return self._amount == other._amount
