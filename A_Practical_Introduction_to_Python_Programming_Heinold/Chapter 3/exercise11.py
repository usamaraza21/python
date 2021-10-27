import math
"""
Write a program that asks the user to enter a weight in kilograms. The program should
convert it to pounds, printing the answer rounded to the nearest tenth of a pound

"""
weight=eval(input('Enter your weight in kilogram\n'))
pound = math.floor(weight * 2.2)
print(pound)