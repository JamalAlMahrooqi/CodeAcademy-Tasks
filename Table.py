# 
# # counts=[
# #     [0,3,0],
# #     [0,0,1],
# #     [0,0,1],
# #     [1,0,0],
# #     [0,0,1],
# #     [3,1,1],
# #     [0,1,0],
# #     [1,0,1]
# #     ]
# # 
# # x=counts[1][2]
# # print(x)
# import random as r
# medals=3#row
# countries=8#column
# table=[]
# for i in range(medals):
#     row=[r.randint(0,99)]*countries
#     table.append(row)
#     print (table)
# x=table[0][1]
# print(x)
# #
# x=[[1,2,3],
#    [4,5,6]]
# 
# for i in range(2):
#     for j in range (3):
#         print(x[i][j],end=' ')
#     print()
#     
#
# 

# table=[[i+1]*3 for i in range (3)]
# 
# for i in range (3):
#     for j in range(3):
#         print (table[i][j],end=' ')
#     
#     print()

# table=[[0]*3 for i in range (3)]
# 
# for i in range(3):#row
#     for j in range (3):#col
#         table[i][j]=i+1
#         print(table[i][j],end=' ')
#     print()
#     
#
# rows=int(input("Enter rows: "))
# col=int(input("Enter columns: "))
# 
# table=[[0]*col for i in range(rows)]
# 
# for i in range(rows):
#     for j in range (col):
#         x=int(input("Enter a value : " ))
#         table[i][j]=x
#         
# for i in range (rows):
#     for j in range(col):
#         print(table[i][j],end=' ')
#     print()
# 
# table=[[0]*4 for i in range(4)]
# 
# for i in range (4):
#     for j in range(4):
#         if i==j:
#             table[i][j]=1
#         if i>j:
#             table[i][j]=2
#         else:
#             table[i][j]=0
#             
# for i in range (4):
#     for j in range(4):
#         print(table[i][j],end=' ')
#     print()
# 


# table=[[0]*4 for i in range(4)]
# 
# for i in range (4):
#     for j in range(4):
#         if i==j:
#             table[i][j]=1
#             table[i][j-2]=1
#         
# for i in range (4):
#     for j in range(4):
#         print(table[i][j],end=' ')
#     print()

table=[[0]*4 for i in range(4)]

for i in range (4):
    for j in range(4):
        if i+j2==0:
            table[i][j]=1
            table[i][j-2]=1
        
for i in range (4):
    for j in range(4):
        print(table[i][j],end=' ')
    print()