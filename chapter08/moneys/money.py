from abc import ABCMeta, abstractmethod


class Money(metaclass=ABCMeta):
    """Money class"""

    def __init__(self, amount: int):
        self._amount = amount

    def __eq__(self, other):
        return self._amount == other._amount and \
            self.__class__.__name__ == other.__class__.__name__

    @abstractmethod
    def times(self, multiplier: int):
        raise NotImplementedError()

    @staticmethod
    def dollar(amount: int):
        """"create dollar"""
        from .dollar import Dollar
        return Dollar(amount)
    
    @staticmethod
    def franc(amount: int):
        """"create franc"""
        from .franc import Franc
        return Franc(amount)


