# -*- coding: utf-8 -*-
#
# Author: taketoshi.kazusa
#
import sys,os
sys.path.append(os.pardir)

import pytest
from money.dollar import Dollar
from money.franc import Franc


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

    def test_Equality(self, dollar):
        dollar1 = dollar(5)
        dollar2 = dollar(5)
        assert dollar1._amount == dollar2._amount


        dollar1 = dollar(5)
        dollar2 = dollar(6)
        assert dollar1._amount != dollar2._amount





        
