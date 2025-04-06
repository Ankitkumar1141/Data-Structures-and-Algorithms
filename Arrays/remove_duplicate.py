### Function to remove duplicate elements
def remove_duplicate(arr):

    new_arr = []
    ## Edge cases
    if len(arr) == 0:
        return "Empty array"
    elif len(arr) == 1:
        new_arr.append(arr[0])
        return new_arr
    
    i = 0
    flag = True
    while(i<len(arr)):
        num = arr[i]
        for j in range(i+1,len(arr)):
            if num == arr[j]:
                flag = False
            else:
                flag = True
        if flag == False:
            i= i+1
            flag = True
        else:
            new_arr.append(num)
            i = i+1
            flag = True
    return new_arr

print(remove_duplicate([3]))
print("/n")
print(remove_duplicate([]))
print(remove_duplicate([1,2,3,4,5,6,6]))
print(remove_duplicate([1,2,3,4,5,6,7]))