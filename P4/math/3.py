#Write a Python program to calculate the area of regular polygon.
"""
Input number of sides: 4
Input the length of a side: 25
The area of the polygon is: 625
"""
from math import *
n = int(input())
l = int(input())
print("Input number of sides:", n)
print("Input the length of a side:", l)
a = l/(2*tan(radians(180/n)))
A = (n * l * a)*1/2
print("The area of the polygon is:", A)