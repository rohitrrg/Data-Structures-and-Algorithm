def search(arr, n, x):
    for i in range(n):
        if arr[i] == x:
            return i
    return -1

arr = [2,3,4,10,40]
n = len(arr)
x = 10

r = search(arr, n, x)
if r != -1:
    print('Element is present at index', r)
else:
    print('Element is not present in array.')
    