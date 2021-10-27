from math import *
from random import *
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 21:30:12 2021

@author: Usama
"""

"""
4. Write a program that generates a random decimal number between 1 and 10 with two decimal
places of accuracy. Examples are 1.23, 3.45, 9.80, and 5.00
"""
x=round(uniform(1,10),2)
print(x)