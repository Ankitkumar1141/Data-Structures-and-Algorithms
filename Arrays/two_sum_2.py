"""Optimal approach
Find the pairs whose sum is equal to the target sum"""

## Input array must be sorted in ascending order

arr = [1,2,3,4,5,6,7,8,9]
target = 9
def find_pairs(arr,target):
    ## Check if the array is empty
    if len(arr) == 0:
        print("Array is empty")
    else:
        start = 0
        end = len(arr)-1

        while(start < end):
            if arr[start] + arr[end] == target:
                return [arr[start],arr[end]]
            elif arr[start] + arr[end] > target:
                end = end -1
            else:
                start  = start + 1
    return -1

print(find_pairs(arr,target))