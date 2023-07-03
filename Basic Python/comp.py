# # # string=input("Enter a number in the format of (xxx)xxx-xxxx")
# # # valid=len(string)==13 
# # # position=0
# # # while valid and position<len(string):
# # #     if position==0:
# # #         valid=string[position]=="("
# # #     elif position==4:
# # #         valid=string[position]==")"
# # #     elif position==8:
# # #         valid=string[position]=="-"
# # #     else:
# # #         valid=string[position].isdigit()
# # #     position+=1
# # #     
# # # if valid:
# # #     print("Valid")
# # # else:
# # #     print("Invalid")
# # 




password=input("""Enter a passwrod that contains that has following:
8 charaters
Contains a lower case
contains an uppercase
contains num
a special char (@,$,#,_)
""" 
)

contains_lowercase = False
contains_uppercase = False
contains_digit = False
contains_special = False

for char in password:
    if char.islower():
        contains_lowercase = True
    elif char.isupper():
        contains_uppercase = True
    elif char.isdigit():
        contains_digit = True
    elif char in "@$#_":
        contains_special = True

if len(password) < 8 or not contains_lowercase or not contains_uppercase or not contains_digit or not contains_special:
    print("Password is not valid.")
else:
    print("Password is valid.")

    
    
    
    
# #     
# import random as r
# 
# answer=(r.randint(1,100))
# guess=input("Guess a number: ")
# while int(guess)>100 or int(guess)<1:
#     print("Out of the range")
#     break
# while answer!=guess:
#     if int(guess)==answer:
#         print("Congratulations! You Win.")
#         break
#     elif int(guess)<answer:
#         print("Go Higher!")
#         guess=input("Guess again: ")
#     else:
#         print("Go lower!")
#         guess=input("Guess again: ")
# 





for i in range (1,100):
    if i==4:
        continue
    else:
        if i==50:
            break
    print(i)
