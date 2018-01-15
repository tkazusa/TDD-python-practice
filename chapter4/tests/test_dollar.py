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
        assert dollar(5).times(2) == dollar(10)

        assert dollar(5).times(3) == dollar(15)

    def test_Equality(self, dollar):
        dollar1 = dollar(5)
        dollar2 = dollar(5)
        assert dollar1._amount == dollar2._amount


        dollar1 = dollar(5)
        dollar2 = dollar(6)
        assert dollar1._amount != dollar2._amount





        
