from .money import Money

class Franc(Money):
    """ franc class"""
    def times(self, multiplier: int):
        return Franc(self._amount * multiplier)
