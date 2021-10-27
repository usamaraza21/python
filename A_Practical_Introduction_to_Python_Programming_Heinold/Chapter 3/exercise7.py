from math import *
from random import *
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 01:34:28 2021

@author: Usama
"""

"""
7. Write a program that asks the user to enter an angle between −180◦
and 180◦
. Using an
expression with the modulo operator, convert the angle to its equivalent between 0 and 360

"""

angle=eval(input('enter angle between -180 to 180\n'))
a=(angle+180)%180
print(a)