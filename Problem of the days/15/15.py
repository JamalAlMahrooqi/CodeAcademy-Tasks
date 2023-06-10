# -*- coding: utf-8 -*-
"""
@author: jamal
discount program
"""

def Discount(x,y):
    discount = x - (x * y / 100)
    return discount

amount=int(input("Enter the original amount: "))
percentage=int(input("Enter the discount precentage: "))

print(f"The price after the discount is {int(Discount(amount,percentage))}")
