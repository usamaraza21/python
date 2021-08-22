import math
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 20:47:33 2021

@author: Usama
"""

"""
15. Write a program that prints a giant letter A like the one below. Allow the user to specify how
large the letter should be.


"""
var=0
large=eval(input('how large the letter A?\n'))
print(' '*large,'*')
for i in range(1,math.floor(large/2)):
    var=large+1-i
    var2=i*2-1
    print(' '*var,'*',' '*var2,'*',sep='')
    
    
print(' '*(var-2),'*'*(var2+4))

for j in range(math.floor(large/2)+1,large):
    var=large+1-j
    var2=j*2-1
    print(' '*var,'*',' '*var2,'*',sep='')