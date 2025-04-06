### Function to check whether the array contains duplicate or not
def check_duplicate(arr):
    if len(arr) == 0:
        return "Empty array"
    elif len(arr) == 1:
        return "Do not contain duplicate elements"
    flag = True

    for i in range(0,len(arr)):
        num = arr[i]
        for j in range(i+1,len(arr)):
            if num == arr[j]:
                flag = True
                break
            else:
                flag = False
    if flag == True:
        return "Contains duplicate elements"
    if flag == False:
        return "Do not contain duplicate elements"
    
print(check_duplicate([1]))
print(check_duplicate([]))
print(check_duplicate([1,2,3,4,5,6,6]))
print(check_duplicate([1,2,3,4,5,6,7]))