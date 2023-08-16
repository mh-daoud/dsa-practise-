# Merge sort is defined as a sorting algorithm that works by dividing an array into smaller subarrays,
# sorting each subarray, and then merging the sorted subarrays back together to form the final sorted array.
# time complexity O(nLog(n)) , space complexity O(n)
import math


def mergeSort(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = []
    R = []
    i = 0
    j = 0

    while i < n1:
        L.append(arr[l + i])
        i += 1
    while j < n2:
        R.append(arr[m + 1 + j])
        j += 1

    i = 0
    j = 0
    k = l
    while (i < n1 and j < n2):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def sort(arr, l, r):
    if l < r:
        m = math.floor(l + ((r - l)/2))
        sort(arr, l, m)
        sort(arr, m+1, r)
        mergeSort(arr, l, m, r)


nums = [3, 9, 13, 2, 1, 7, 5, 4, 17, 21, 3]
print(nums)
sort(nums, 0, len(nums) - 1)
print(nums)
