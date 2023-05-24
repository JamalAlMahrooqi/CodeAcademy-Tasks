"""
shift the list from left x number of times
"""

#input from user
flag = True
my_list = []

flag = True
my_list = []

while flag:
    x = input("Enter values to put in the list, type 'q' to stop: ")
    if str(x).lower() == "q":
        flag = False
    else:
        my_list.append(int(x))
        
        
shift_amount = int(input("How many times do you shift the values: ")) 

my_list = my_list[shift_amount:] + my_list[:shift_amount]

print("Shifted list:", my_list)


