## Find the maximum element of the given array

arr = [4,7,-28,8,6,-9,0]
max = arr[0]
size = len(arr)
for i in range(0,size):
    if arr[i] > max:
        max = arr[i]

print("Maximum value present in array is",max)
