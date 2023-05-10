s=input("Enter a string: ")


if len(s)%2==0:
    pos=int(len(s)/2)
    print (s[pos]+ s[pos+1])
else:
    pos=int(len(s)/2)
    print(s[pos])