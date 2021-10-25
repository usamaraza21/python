# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 10:00:02 2021

@author: Usama
"""

"""
8. Write a program that asks the user for their name and how many times to print it.
   The program should print out the user’s name the specified number of times
"""

name=input('whats your name?\n')
count=eval(input('how many times want to print your name?\n'))
for i in range(count):
    print(i,'hi',name)