# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 18:27:14 2021

@author: Usama
"""

"""
11. Use a for loop to print a box like the one below. Allow the user to specify how wide and how
high the box should be.
*******************
*                 *
*                 *
*******************
"""
wide=eval(input('insert width of box\n'))
high=eval(input('insert height of box\n'))
for i in range(1):
    print('*'*wide)
for j in range(1,high-2):
    print("*"," "*(wide-4),'*')
for i in range(1):
    print('*'*wide)