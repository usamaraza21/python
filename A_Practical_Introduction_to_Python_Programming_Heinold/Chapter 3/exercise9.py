# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 22:08:11 2021

@author: Usama
"""

"""
9. Write a program that asks the user for an hour between 1 and 12 and for how many hours in
the future they want to go. Print out what the hour will be that many hours into the future.
An example is shown below.
Enter hour: 8
How many hours ahead? 5
New hour: 1 o'clock
"""

hrs=eval(input('enter  hours b/w 1-12 : \n'))
ahead=eval(input('how many hours ahead'))
newhour=(hrs+ahead)%12
print('new hour is: ',newhour,'o`clock')