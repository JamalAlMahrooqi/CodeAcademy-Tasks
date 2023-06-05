# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 15:34:41 2023

@author: jamal
"""


"""
πr2h
3
"""
import math
def cone_volume(h,r):
    return math.pi* r**2* h/3


height=(int(input("Enter the height of a cone: ")))
radius=(int(input("Enter the radius of a cone: ")))

print("{:.2f}".format(cone_volume(height, radius)))

        