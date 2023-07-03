message=input("Enter a message")
length=len(message)
for i in range (length):
    original=ord(message[i])
    new=original+3
    print(chr(new),end="")