# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 16:15:09 2023

@author: jamal
"""


text_to_find = 'CodeAcademy'
text_to_search = input("Enter a text: ")

words_split = text_to_search.split()

if text_to_find in words_split:
    index = words_split.index(text_to_find)+1
    print(f"{text_to_find} is found at index: {index}")
else:
    print(f"{text_to_find} is not found!")


