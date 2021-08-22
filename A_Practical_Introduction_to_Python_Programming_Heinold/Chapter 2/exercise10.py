# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 18:12:21 2021

@author: Usama
"""

"""
Use a for loop to print a box like the one below. Allow the user to specify how wide and how
high the box should be. [Hint: print('*'*10) prints ten asterisks.]
*******************
*******************
*******************
*******************
"""

wide=eval(input('insert width of your box\n'))
high=eval(input('insert height of your box\n'))
for i in range(high):
    print('*'*wide)