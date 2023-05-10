Value=int(input("Enter a value: "))
ans=input("Is the value you entered in celcius or fahrenheit (answer with c/f)")
if ans=="c":
    convert=(Value*9/5) + 32
    print(str(convert) +" Fahrenheit")
else:
        convert= (Value-32) * 5/9
        print(str(convert) +" Celcius")
