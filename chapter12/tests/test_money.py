# -*- coding: utf-8 -*-
#
# Author: taketoshi.kazusa
#
import sys,os
sys.path.append(os.pardir)

import pytest
from moneys.money import Money
from moneys.bank import Bank


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
        assert money.dollar(5) == money.dollar(5)
        assert money.dollar(5) != money.dollar(6)
        assert money.franc(5) != money.dollar(6)

    def test_currency(self):
        assert Money.franc(1).currency() == "CHF"
        assert Money.dollar(1).currency() == "USD"
    
    def test_SimpleAddition(self):
        assert Money.dollar(5).plus(Money.dollar(5)) == Money.dollar(10)
        
        five = Money.dollar(5)
        sumattion = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(sumattion, "USD")
        assert Money.dollar(10) == reduced

