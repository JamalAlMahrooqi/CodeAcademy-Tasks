def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
         # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
         # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
        # means x is present at mid
        else:
            return mid
    # If we reach here, then the element was not present
    return -1
 

list2=[2,4,1,5,6,8,10]
target=int(input("Enter a target to search:  "))


x=binary_search(list2,target)
print(list2[x])
print(list2[x]**1/2)



