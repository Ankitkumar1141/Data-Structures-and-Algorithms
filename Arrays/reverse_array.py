"""Write a program to reverse without using any extra array"""

arr = [1,2,3,4,5,6,7]

print("Original array is",arr)

def swap(arr):
    start = 0
    end = len(arr)-1
    while(start < end):
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
    return arr

print("Reversed array is ",swap(arr))


