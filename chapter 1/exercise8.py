# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 17:09:04 2021

@author: Usama
"""

"""
8. Write a program that asks the user to enter three numbers (use three separate input statements). Create variables called total and average that hold the sum and average of the
three numbers and print out the values of total and average.
"""
num1=eval(input('enter first number\n'))
num2=eval(input('enter second number\n'))
num3=eval(input('enter third number\n'))
total = num1 + num2 + num3
average = total/3
print('given numbers total is',total,'and average is',average)