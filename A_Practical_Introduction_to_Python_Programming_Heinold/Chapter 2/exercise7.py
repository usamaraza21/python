# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 09:46:08 2021

@author: Usama
"""

"""
7. Write a program that uses exactly four for loops to print the sequence of letters below.
AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG
"""

for i in range(10):
    print('A',end='')
for j in range(7):
    print('B',end='')
for k in range(4):
    print('C',end='')
    print('D',end='')
print('E',end='')
for l in range(6):
    print('F',end='')
print('G')