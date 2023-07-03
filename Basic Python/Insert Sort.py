def insertionSort(name,age):
    for step in range(1,len(age)):
        key1=name[step]
        key=age[step]
        j=step-1
        
        while j>=0 and key<age[j]:
            name[j+1]=name[j]
            age[j+1]=age[j]
            j=j-1
            
        name[j+1]=key1
        age[j+1]=key
        
list1=["Said,25","Majid,19","Salim,32","Ali,21","Sultan,29"]
age=[]
name=[]

#split
for i in range(len(list1)):
    x=(list1[i].split(","))
    age.insert(i,x[1])
    name.insert(i,x[0])

#change to int
for i in range(0, len(age)):
    age[i] = int(age[i])

print(name)
print(age)
print()

insertionSort(name,age)

print(age)
print (name)

# #age
# for i in range(len(list1)):
#     x=(list1[i].split(","))
#     for i in x:
#         list2.append(x[1]) 
# for i in range(0, len(list2)):
#     list2[i] = int(list2[i])
# list2 = list(set(list2))
# insertionSort(list2)
# print(list2)
# 
# #name
# for i in range(len(list1)):
#     x=(list1[i].split(","))
# 
#     for i in x:
#         name.append(x[0])
# name = list(set(name))
# print(name)



