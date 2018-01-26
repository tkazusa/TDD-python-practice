# -*- coding: utf-8 -*-
#
# Author: taketoshi.kazusa
#
import sys,os
sys.path.append(os.pardir)

import pytest
from moneys.money import Money


class TestMoney(object):
    """Test for money class"""
    
  
    @pytest.fixture
    def money(request):
        return Money

    def test_DollarMultiplication(self, money):
        assert money.dollar(5).times(2) == money.dollar(10)
        assert money.dollar(5).times(3) == money.dollar(15)

    def test_FrancMultiplication(self, money):
        assert money.franc(5).times(2) == money.franc(10)
        assert money.franc(5).times(3) == money.franc(15)

    def test_Equality(self, money):
        assert money.dollar(5)._amount == money.dollar(5)._amount
        assert money.dollar(5)._amount != money.dollar(6)._amount
        assert money.franc(5)._amount == money.franc(5)._amount
        assert money.franc(5)._amount != money.franc(6)._amount
        assert money.franc(5)._amount != money.dollar(6)._amount

    def test_currency(self):
        assert Money.franc(1).currency() == "CHF"
        assert Money.dollar(1).currency() == "USD"

    def test_differentclass_equality(self):
        assert Money(10, "CHF") == Money.franc(10)


