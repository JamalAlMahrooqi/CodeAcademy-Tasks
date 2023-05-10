memory=input("Enter your computer memory: ")
file_size=input("Enter a file size: ")
number_of_files=input("Enter the number of files: ")

if(int(file_size)*int(number_of_files)<=int(memory)):
    print("The file can be stored")
else:
    print("The file can't be stored")