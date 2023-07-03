# square=lambda x:x**2
# print(square(2))
# 

people=[
    {'Name':'Johnny','Age':28},
    {'Name':'Mary','Age':23},
    {'Name':'Bob','Age':35},
    {'Name':'Alice','Age':32},
    ]


people.sort(key=lambda x: x['Age'])

for i in people:
    for key in i.values():
        print (key,end='  ')

