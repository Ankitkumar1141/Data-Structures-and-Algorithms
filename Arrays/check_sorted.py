## Function to check whether the array is sorted or not
def check_sorted(arr):
    if len(arr) == 0:
        return "Empty array"
    elif len(arr) == 1:
        return "Sorted array"
    flag = True
    for i in range(0,len(arr)-1):
        if arr[i] > arr[i+1]:
            flag = False
            break
        else:
            flag = True
    if flag == True:
        return "Sorted array"
    if flag == False:
        return "Unsorted array"

print(check_sorted([1,2,3,4,5]))
print(check_sorted([6,4,2,8,9]))

    
        
