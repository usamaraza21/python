# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 19:04:30 2021

@author: Usama
"""

"""
Use a for loop to print an upside down triangle like the one below. Allow the user to specify
how high the triangle should be.
****
***
**
*

"""

high=eval(input('insert the height\n'))
for i in range(high,0,-1):
    print('*'*i)