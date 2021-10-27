from math import *
from random import *
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 21:21:10 2021

@author: Usama
"""

"""
Q2. Write a program that generates a random number, x, between 1 and 50, a random number y
between 2 and 5, and computes x^y.
"""
x=randint(1,50)
y=randint(2,5)
print(x,'^',y,' =',x**y)