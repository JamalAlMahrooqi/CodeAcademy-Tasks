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
# # 
# # 
# # s=input("""Enter a passwrod that contains the following:
# # 8 charaters
# # Contains a lower case
# # contains an uppercase
# # contains num
# # Special char
# # """)
# # special=["@","$","#","_"]
# # contains_num=False
# # contains_char=False
# # contains_lower=False
# # contains_num=False
# # pos=0
# # 
# # length=len(s)
# # for i in range(length):
# #         if(s[i] in special or
# #            s[i].islower or
# #            s[i].isupper or
# #            isinstance(s[i],int)or
# #            isinstance(s[i],str)
# #            ):
# #             valid=True
# #         else:
# #             valid=False
# # 
# # if valid:
# #     print("Valid")
# # else:
# #     valid=False
# #     print("Invalid")
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