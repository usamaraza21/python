from random import *
from math import *
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 01:22:07 2021

@author: Usama
"""

"""
5. Write a program that generates 50 random numbers such that the first number is between 1
and 2, the second is between 1 and 3, the third is between 1 and 4, . . . , and the last is between
1 and 51.
"""

for i in range(2,52):
    x=randint(1,i)
    print('number taken between 1 and',i,'is :',x)