from .money import Money

class Dollar(Money):
    """ dollar class"""
    def times(self, multiplier: int):
        return Dollar(self._amount * multiplier)

