# -*- coding: utf-8 -*-
"""

@author: jamal
"""


flag = True
my_array = []

while flag:
    x = input("Enter values to put in the list, type 'q' to stop: ")
    if str(x).lower() == "q":
        flag = False
    else:
        my_array.append(int(x))
        

unique_values = []
repeated_values = set()

for element in my_array:
    if element in repeated_values:
        continue
    elif element in unique_values:
        unique_values.remove(element)
        repeated_values.add(element)
    else:
        unique_values.append(element)

first_non_repeated = unique_values[0] if unique_values else None

print(first_non_repeated)
