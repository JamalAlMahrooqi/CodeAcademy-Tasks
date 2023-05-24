# Print the most repeated value
flag = True
list1 = []
while flag:
    x = input("Enter values to put in the list, type 'q' to stop: ")
    if x.lower() == "q":
        flag = False
    else:
        list1.append(int(x))

most_repeated_value = None
max_count = 0

for i in range(len(list1)):
    count = 0
    for j in range(i + 1, len(list1)):
        if list1[i] == list1[j]:
            count += 1
    if count > max_count:
        max_count = count
        most_repeated_value = list1[i]

print(f"Most repeated value: {most_repeated_value}")
