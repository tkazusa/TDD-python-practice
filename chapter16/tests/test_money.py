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

    def test_currency(self, money):
        assert money.franc(1).currency() == "CHF"
        assert money.dollar(1).currency() == "USD"
    
    def test_SimpleAddition(self, money):
        five = money.dollar(5)
        summation = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(summation, "USD")
        assert money.dollar(10) == reduced

    def test_PlusReturnsSum(self, money):
        five = money.dollar(5)
        result = five.plus(five)
        assert five == result.augend()
        assert five == result.addend()

    def test_ReduceSum(self, money):
        summation = Summation(money.dollar(3), money.dollar(4))
        bank = Bank()
        result = bank.reduce(summation, "USD")
        assert result == money.dollar(7)

    def test_Reducemoney(self, money):
        bank = Bank()
        result = bank.reduce(money.dollar(1), "USD")
        assert money.dollar(1) == result

    def test_ReducemoneyDifferentCurrency(self, money):
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        result = bank.reduce(money.franc(2), "USD")
        assert money.dollar(1) == result
    
    def test_mixed_addition(self, money):
        five_bucks = money.dollar(5)
        ten_francs = money.franc(10)
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        result = bank.reduce(five_bucks.plus(ten_francs), "USD")
        assert money.dollar(10) == result

    def test_TotalPlusmoney(self, money):
        five_bucks = money.dollar(5)
        ten_francs = money.franc(10)
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        summation = Summation(five_bucks, ten_francs).plus(five_bucks)
        result = bank.reduce(summation, "USD")
        assert money.dollar(15) == result

    def test_TotalTimes(self, money):
        five_bucks = money.dollar(5)
        ten_francs = money.franc(10)
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        summation = Summation(five_bucks, ten_francs).times(2)
        result = bank.reduce(summation, "USD")
        assert money.dollar(20) == result
