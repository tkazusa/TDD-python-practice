# -*- coding: utf-8 -*-
#
# Author: taketoshi.kazusa
#
import sys,os
sys.path.append(os.pardir)

import pytest
from dollar import Dollar


class TestMoney(object):
    """Test for money class"""
   
    @pytest.fixture
    def dollar(request):
        return Dollar

    def test_Multiplication(self, dollar):
        expected = 10
        product = dollar(5).times(2)
        actual = product.amount
        assert actual == expected

        expected = 15
        product = dollar(5).times(3)
        actual = product.amount
        assert actual == expected

    def test_Equality(self, dollar):
        dollar1 = dollar(5)
        dollar2 = dollar(5)
        assert dollar1.amount == dollar2.amount


        dollar1 = dollar(5)
        dollar2 = dollar(6)
        assert dollar1.amount != dollar2.amount





        
