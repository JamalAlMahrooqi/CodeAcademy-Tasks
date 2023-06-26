# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:07:14 2023

@author: jamal
write a function with two parameters one defines the length and the other defines the devisible increment
"""


def Multiples(num, length):
    answer = []
    for i in range(1, length+1):
        answer.append(i * num)
    return answer

    
print(Multiples(3, 7))

print(Multiples(10, 4))