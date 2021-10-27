import math
"""
14. Write a program that asks the user to enter an angle in degrees and prints out the sine of that
angle

"""

angle = eval(input("enter angle in degrees\n"))
a = math.sin(math.radians(angle)) 
print("sin(",angle,") = ",a,sep="")