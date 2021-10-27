# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 21:56:51 2021

@author: Usama
"""

"""
8. Write a program that asks the user for a number of seconds and prints out how many minutes
and seconds that is. For instance, 200 seconds is 3 minutes and 20 seconds. [Hint: Use the //
operator to get minutes and the % operator to get seconds.]
"""

seconds=eval(input('enter any number in seconds\n'))
min=seconds//60
sec=seconds%60
print(seconds,' is ',min,' minutes ',sec,'seconds')