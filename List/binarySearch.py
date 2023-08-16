def insertionSort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def binarySearch(arr, x, l, r):

    if l <= r:
        m = l + ((r - l) // 2)
        if arr[m] == x:
            return m
        elif arr[m] > x:
            return binarySearch(arr, x, l, m-1)
        else:
            return binarySearch(arr, x, m+1, r)
    return -1


nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
insertionSort(nums)
index = binarySearch(nums, 9, 0, len(nums)-1)
print(nums, index)
