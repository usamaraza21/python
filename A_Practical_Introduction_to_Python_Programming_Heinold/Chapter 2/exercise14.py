# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 19:31:01 2021

@author: Usama
"""

"""
4. Use for loops to print a diamond like the one below. Allow the user to specify how high the
diamond should be.
   *
  ***
 *****
*******
 *****
  ***
   *


"""

high=eval(input('insert height\n'))
for i in range(1,high+1):
    print(' '*(high-i),' *'*i)
for j in range(high-1):
    print(' '*(j+1),' *'*(high-1-j))
    