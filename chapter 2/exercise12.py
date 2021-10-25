# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 19:00:21 2021

@author: Usama
"""

"""
 Use a for loop to print a triangle like the one below. Allow the user to specify how high the
triangle should be.
*
**
***
****

"""
high=eval(input('how high the triangle is?\n'))
for i in range(1,high+1):
    print('*'*i)