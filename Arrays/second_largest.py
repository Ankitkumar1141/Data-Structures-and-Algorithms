## Find the second largest element of the array

arr = [4,7,-28,8,6,-9,0]
max = arr[0]
sec_max = arr[0]

for i in range(0,len(arr)):
    if arr[i] > max:
        max = arr[i]

for i in range(0,len(arr)):
    if arr[i] > sec_max and arr[i] < max:
        sec_max = arr[i]

print(f"Largest element is {max} and second largest element is {sec_max}")


## Time complexity : 0(n)
## Space complexity : 0(1)