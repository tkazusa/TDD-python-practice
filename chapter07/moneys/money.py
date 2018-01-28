class Money(object):
    """Money class"""
    def __init__(self, amount: int):
        self._amount = amount

    def __eq__(self, other):
        return self._amount == other._amount and \
            self.__class__.__name__ == other.__class__.__name__




