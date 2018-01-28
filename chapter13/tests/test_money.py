# -*- coding: utf-8 -*-
#
# Author: taketoshi.kazusa
#
import sys,os
sys.path.append(os.pardir)

import pytest
from moneys.money import Money
from moneys.bank import Bank
from moneys.sum import Summation

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
        five = Money.dollar(5)
        summation = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(summation, "USD")
        assert Money.dollar(10) == reduced

    def test_PlusReturnsSum(self):
        five = Money.dollar(5)
        result = five.plus(five)
        assert five == result.augend()
        assert five == result.addend()

    def test_ReduceSum(self):
        summation = Summation(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(summation, "USD")
        assert result == Money.dollar(7)

    def test_ReduceMoney(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1), "USD")
        assert Money.dollar(1) == result
