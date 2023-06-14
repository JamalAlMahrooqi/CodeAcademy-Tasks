# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 13:50:03 2023

@author: jamal
"""


def split_text(x, y):
    if y <= 0:
        return "Error"
    
    if len(x) % y != 0:
        return "Error"
    
    count = len(x) // y
    
    pairs = []
    for i in range(0, len(x), count):
        pair = x[i:i+count]
        pairs.append(pair)
    
    return pairs

print(split_text("Establish", 3))
print(split_text("Recollective", 6))
print(split_text("Strongest", 4))
