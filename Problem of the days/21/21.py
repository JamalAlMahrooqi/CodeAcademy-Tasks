# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 16:39:16 2023

@author: jamal
"""

texts = ["The Real one", "An Arrangement", "A Royalty", "Establishment", "The Avengers", "An Occupation"]
ban_words=["The","A","An"]
modified_texts = []
for text in texts:
    #print(text)
    words = text.split()
    modified_words = []
    modified_text = ""
    for word in words:
        if word not in ban_words:
            modified_words.append(word)
    modified_text += word
    modified_texts.append(modified_text)
print(sorted(modified_texts))
