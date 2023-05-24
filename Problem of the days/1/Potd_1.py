#write a program that compares between 3 numbers and provides the biggest number and tells the user if the numbers  are equal

a,b,c =input("Enter 3 numbers")
list=[a,b,c]
print(a," ",b," ",c)

if (a==b==c):
    {
       print("The numbers are equal") 
    }
else:
    m=max(list)
    print(m," is the maximum number")
