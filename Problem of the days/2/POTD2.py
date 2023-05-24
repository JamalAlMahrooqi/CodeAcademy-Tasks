import math

num_matrices = int(input("Enter the number of matrices: "))
matrices = []


for i in range(num_matrices):
    matrix_input = input(f"Enter the values for matrix {i+1}: ")
    matrix = [int(val) for val in matrix_input.split()]
    matrices.append(matrix)
    
#y values
y_coords = []
for matrix in matrices:
    for i in range(1, len(matrix), 2):
        y_coords.append(matrix[i])

#ymin/ymax
ymin = min(y_coords)
ymax = max(y_coords)




#calculating lengths
lengths=[]
for vector in matrices:
    for i in range(0, len(vector)-2, 2):
        x = math.sqrt((vector[i+2]-vector[i])**2 + (vector[i+3]-vector[i+1])**2)
        lengths.append(x)

print(lengths)



#calculating slope
vectors = matrices
slopes = []
for vector in vectors:
    for i in range(0, len(vector)-3, 4):
        x1, y1, x2, y2 = vector[i:i+4]
        try:
            slope = (y2 - y1) / (x2 - x1)
        except ZeroDivisionError:
            slope = float('inf')
        
        slopes.append(slope)      
print(slopes)


print("Y min is: "+str((ymin)))
print("Ymax is: "+str((ymax)))

