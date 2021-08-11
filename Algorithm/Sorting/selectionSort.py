def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_ind = i
        for j in range(i+1, n):
            if arr[min_ind]>arr[j]:
                min_ind = j
        #swap
        arr[min_ind], arr[i] = arr[i], arr[min_ind]


arr = [64,25,12,22,11]
selectionSort(arr)
print(arr)