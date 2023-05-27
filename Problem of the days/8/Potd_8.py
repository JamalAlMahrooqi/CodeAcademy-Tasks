
"""

@author: jamal
"""

table = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]


num_rows = len(table)
num_cols = len(table[0])


diagonal_sum1 = 0
diagonal_values1 = []
diagonal_sum2 = 0
diagonal_values2 = []


for i in range(min(num_rows, num_cols)):
    y=table[i][i]
    diagonal_values1.append(str(y))
    diagonal_sum1 += y
    
for i in range(num_rows):
    x=value = table[i][num_cols - 1 - i]
    diagonal_values2.append(str(x))
    diagonal_sum2 += x
    
subs = abs(diagonal_sum1-diagonal_sum2)

output1 = " + ".join(diagonal_values1) + " = " + str(diagonal_sum1)
output2 = " + ".join(diagonal_values2) + " = " + str(diagonal_sum2)
output3 = "| " + str(diagonal_sum1) + ' - ' + str(diagonal_sum2) + ' | ' + "=" + str(subs)


print(output1)
print(output2)
print(output3)


