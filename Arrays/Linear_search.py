### Linear search
arr = [7,5,10,47,35,9,7]
target = 47

def linear_search(arr,target):
    size = len(arr)
    found = False
    ans = -1
    for i in range(0,size):
        if arr[i] == target:
            found =True
            ans = i
            break
        else:
            found = False
    if found == True:
        print(f"Target element found sucessfully at {ans}th index")
    else:
        print("Not found")

print(linear_search(arr,target))

## Time complexity: 0(n)
## Space complexity: 0(1)