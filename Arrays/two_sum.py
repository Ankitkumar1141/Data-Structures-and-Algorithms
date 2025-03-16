""" Find all pairs of the array elements whose sum is equals to the target"""
arr = [1,2,3,4,5,6,7,8,9]
target_sum = 9

def find_pairs(arr,target_sum):
    pairs = []
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == target_sum:
                pairs.append((arr[i],arr[j]))
    return pairs

result = find_pairs(arr,target_sum)

if result:
    print(f"{result} is the pairs equals to the target sum")
else:
    print("No pairs found")