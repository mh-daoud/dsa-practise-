# Bucket sort is a sorting technique that involves dividing elements into various groups, or buckets.
# These buckets are formed by uniformly distributing the elements. Once the elements are divided into buckets,
# they can be sorted using any other sorting algorithm.
# Finally, the sorted elements are gathered together in an ordered fashion.
# time complexity O(n^2) , space complexity O(n+k) where k is number of buckets

import math


def insertionSort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def bucketSort(arr):
    buckets = []
    k = 10
    max = arr[0]

    for num in arr:
        if max < num:
            max = num
    max += 1
    for bucket in range(k):
        buckets.append([])

    for num in arr:
        buckets[math.floor(k * (num/max))].append(num)

    for bucket in buckets:
        insertionSort(bucket)

    index = 0
    for bucket in buckets:
        for num in bucket:
            arr[index] = num
            index += 1


nums = [3, 9, 13, 2, 1, 7, 5, 4, 17, 21, 3]
print(nums)
bucketSort(nums)
print(nums)
