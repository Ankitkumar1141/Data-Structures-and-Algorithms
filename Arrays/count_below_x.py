## Find the count of elements less than x.
arr = [4,7,-28,8,6,-9,0]

x =6
def count(arr,x):
    count =0
    for i in range(0,len(arr)):
        if arr[i] < x:
            count = count + 1
    return count
print(f"{count(arr,x)} elements are below {x} in the given array")
