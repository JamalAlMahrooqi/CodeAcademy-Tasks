n = 100
perfect_numbers = []

for num in range(1, n + 1):
    div_sum = 0
    for i in range(1, num):
        if num % i == 0:
            div_sum += i
    
    if div_sum == num:
        perfect_numbers.append(num)

print("Perfect numbers up to", n, "are:", perfect_numbers)
