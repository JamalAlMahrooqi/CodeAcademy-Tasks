import functools
# list1=["Dog","cat","Thundercats","wildcats"]
# lower_case=list(filter(lambda i: i.islower(),list1))
# 
# print(lower_case)

# list_of_names=[]
# F=True
# while F:
#     x=str(input("Enter names or q to quit: "))
#    if str(x)=="q":
#        break
#    else:
#        list_of_names.append(x)
# 
# lower_case=list(map(lambda x:x.lower() ,list_of_names))
# print(lower_case)

list3=[3,4,5,6,7]
squares=functools.reduce(lambda total,x:total+x**2,list3,0)

print(squares)
