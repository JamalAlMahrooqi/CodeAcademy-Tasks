file = open("files.txt", 'r')
employee={}
salary=[]


for line in file:
    data = line.split()
    salary.append(float(data[0]))
    employee[data[1]]=data[0]
    
print(salary)
print (employee)



    



