total=0
sum=0
count=0
t=[]
times=input("Enter anything to start")
t.append(times)
for i in t:
    inputStr=input("Enter a value")
    if inputStr=="":
        t.pop()
        break
    else:
        #inputStr=input("Enter a value")
        value=float(inputStr)
        total=total+value
        count=count+1
        t.append(inputStr)

if count >0:
     average=total/count
     print(average)
else:
    average=0.0
