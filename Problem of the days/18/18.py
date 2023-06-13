# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 02:17:01 2023

@author: jamal
"""

def length(lst):
    count = 0
    for item in lst:
        #print(type(item))
        if type(item) == list:
            count += length(item)
        else:
            count += 1
    return count

x = length([1, [2, 3]])
x1 = length([1, 2, 3, [4, 5, [6, 7]]])

print(x)
print(x1)

