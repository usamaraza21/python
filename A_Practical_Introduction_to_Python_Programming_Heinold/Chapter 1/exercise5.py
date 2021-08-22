# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 16:18:47 2021

@author: Usama
"""

"""
Q5. Ask the user to enter a number. Print out the square of the number, but use the 'sep optional'
argument to print it out in a full sentence that ends in a period. Sample output is shown
below.
Enter a number: 5
The square of 5 is 25.
"""
num=eval(input('enter a number\n'))
print('the square of ',num,' is ',num*num,'.',sep='')