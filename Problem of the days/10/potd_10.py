# -*- coding: utf-8 -*-
"""
print the value which is greater or equal to the value next to it from the right
@author: jamal
"""


flag = True
list1 = []
while flag:
    x = input("Enter values to put in the list, type 'q' to stop: ")
    if x.lower() == "q":
        flag = False
    else:
        list1.append(int(x))
        
        
for i in range(len(list1) - 1, 0, -1):
    if list1[i] <= list1[i - 1]:
        print(list1[i],end=' ')
    else:
        print(list1[i],end=' ')
        break
