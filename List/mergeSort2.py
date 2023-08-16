# Merge sort is defined as a sorting algorithm that works by dividing an array into smaller subarrays,
# sorting each subarray, and then merging the sorted subarrays back together to form the final sorted array.
import math


def mergeSort(arr):
    if len(arr) > 1:
        m = len(arr)//2
        L = []
        R = []
        i = 0
        j = m
        while i < m:
            L.append(arr[i])
            i += 1
        while j < len(arr):
            R.append(arr[j])
            j += 1

        mergeSort(L)
        mergeSort(R)

        i = 0
        j = 0
        k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


nums = [3, 9, 13, 2, 1, 7, 5, 4, 17, 21, 3]
print(nums)
mergeSort(nums)
print(nums)
