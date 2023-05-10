Value=int(input("Enter a value: "))
ans=input("Is the value you entered in celcius or fahrenheit (answer with c/f)")
if ans=="c":
    convert=Value*33.8
    print(str(convert) +" Fahrenheit")
else:
    if ans=="f":
        convert=Value/33.8
        print(str(convert) +" Celcius")
