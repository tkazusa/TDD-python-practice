# -*- coding: utf-8 -*-
#
# Author: taketoshi.kazusa
#
import unittest
import dollar

class MoneyTestv(unittest.TestCase):
    """Test for money class"""
    
    def test_Multiplication(self):
        five = dollar.Dollar(5)
        five.times(2)
        self.assertEqual(10, five.amount, "ammount expetced 10")


        
