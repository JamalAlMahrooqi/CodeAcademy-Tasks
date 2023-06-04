# -*- coding: utf-8 -*-
"""

@author: jamal
"""

'''
Check wether you could split the array to see if the sum of the first array is equal to the value in the second array
'''


flag = True
arr=[]

while flag:
    x = input("Enter values to put in the list, type 'q' to stop: ")
    if str(x).lower() == "q":
        flag = False
    else:
        arr.append(int(x))
        

total_sum = sum(arr)
current_sum = 0
first_array = []

for num in arr:
    current_sum += num
    first_array.append(num)

    if current_sum == total_sum - current_sum:
        second_array = arr[len(first_array):]
        print("First array:", first_array)
        print("Add them and u get ")
        print("Second array:", second_array)
        break
else:
    print("Cannot split the array into two parts with equal sums.")

