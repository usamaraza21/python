# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 10:09:14 2021

@author: Usama
"""

"""
The Fibonacci numbers are the sequence below, where the first two numbers are 1, and each
number thereafter is the sum of the two preceding numbers. Write a program that asks the
user how many Fibonacci numbers to print and then prints that many.
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 . . .
"""

number=eval(input('how many fabonacci numbers to print??\n'))
a=0
b=1
print('\n\n\n\n',a,sep='')
print(b)
for i in range(2,number):
    c=a+b
    print(c)
    a=b
    b=c
    
    
    