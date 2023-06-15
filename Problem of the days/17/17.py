# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 03:19:43 2023

@author: jamal

mohammed progress
"""

def progress(lst):
    goal = 0
    prev = 0
    for i in range(len(lst)):
        if lst[i] > lst[prev]:
            goal += 1
        prev = i
    
    return goal

print(progress([2,4,7,10,8,11]))
print(progress([5,7,6,9,8]))
