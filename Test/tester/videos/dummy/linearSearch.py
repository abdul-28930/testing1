def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
        
    return -1
arr = [1,2,4,5,6]
x = 7
print(search(arr,x))