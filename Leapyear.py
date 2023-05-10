input_year=input("Enter a year")
if(int(input_year)%4==0 and input_year%100!= 0 or input_year%400==0):
    print("Leap Year")
else:
    print("Not Leap Year")
