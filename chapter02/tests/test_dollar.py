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
        return Dollar(5)

    def test_Multiplication(self, dollar):
        expected = 10
        product = dollar.times(2)
        actual = product.amount
        assert actual == expected

        expected = 15
        product = dollar.times(3)
        actual = product.amount
        assert actual == expected






        
