# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 13:25:22 2023

@author: jamal
"""

name = input("Enter a name: ")
unique_letters = []

for letter in name:
    if letter in unique_letters:
        continue
    else:
        unique_letters.append(letter)
        
if len(unique_letters)%2==0:
    print("He is a Girl")
else:
    print("He is a Boy")