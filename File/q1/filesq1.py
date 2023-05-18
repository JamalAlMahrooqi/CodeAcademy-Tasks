values = open("q1.txt")
d1=[]
d2=[]

for line in values:
    data=line.split()
    d1.append(int(data[0]))
    d2.append(int(data[1]))

for i in d1:
    distance = d1[0]*d2[0]

for i in d2:
    distance2 = d1[1]*d2[1]


print (distance,distance2)
