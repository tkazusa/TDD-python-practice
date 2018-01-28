# -*- coding: utf-8 -*-
#
# Author: taketoshi.kazusa
#
import sys,os
sys.path.append(os.pardir)

import pytest
from moneys.dollar import Dollar
from moneys.franc import Franc


class TestMoney(object):
    """Test for money class"""
    
  
    @pytest.fixture
    def dollar(request):
        return Dollar
    
    @pytest.fixture
    def franc(request):
        return Franc
 
    def test_DollarMultiplication(self, dollar):
        assert dollar(5).times(2) == dollar(10)
        assert dollar(5).times(3) == dollar(15)

    def test_FrancMultiplication(self, franc):
        assert franc(5).times(2) == franc(10)
        assert franc(5).times(3) == franc(15)

    def test_Equality(self, dollar, franc):
        assert dollar(5)._amount == dollar(5)._amount
        assert dollar(5)._amount != dollar(6)._amount
        assert franc(5)._amount == franc(5)._amount
        assert franc(5)._amount != franc(6)._amount
        assert franc(5)._amount != dollar(6)._amount






        
