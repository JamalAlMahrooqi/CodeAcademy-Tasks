file = open("q2.txt","r")
def factors(n):
    f=[]
    for i in range (1,n+1):
        if n%i==0:
            f.append(i)
    return f
            
list=[]
for line in file:
    data=line.strip()
    list.append(data)


for i in list:
    x = factors(int(i))
    print()
    for i in x:
        print (i,end="")

