# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 22:37:54 2021

@author: Usama
"""

"""
(a) One way to find out the last digit of a number is to mod the number by 10. Write a
program that asks the user to enter a power. Then find the last digit of 2 raised to that
power.
(b) One way to find out the last two digits of a number is to mod the number by 100. Write
a program that asks the user to enter a power. Then find the last two digits of 2 raised to
that power.
(c) Write a program that asks the user to enter a power and how many digits they want.
Find the last that many digits of 2 raised to the power the user entered.
"""

#part a....
pow=eval(input('enter number for power\n'))
a=(2**pow)
lastdigit=a%10
print('2^',pow,' is = ',a,sep='')
print('last digit of 2^',pow,' is : ',lastdigit,sep='' )

#part b....
last2digit=a%100
print('last two digit of 2^',pow,' is : ',last2digit,sep='')

#part c....

digit=eval(input('how many digits you want\n'))
b=(10**digit)
x=(a%b)
print('last ',digit,' digit of 2^',pow,' is : ',x,sep='' )