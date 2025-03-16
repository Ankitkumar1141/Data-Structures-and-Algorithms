## Calculate the sum of all element of an array
arr = [3,6,4,17,39,4,0]
sum = 0
for i in range(0,len(arr)):
    sum = sum + arr[i]
print("Sum of the array elements is",sum)


## Function to find the product of array
def product(arr):
    size = len(arr)
    ans = 1
    for i in range(0,size):
        ans = ans*arr[i]
    return ans

print("Product of the array elements is ",product(arr))