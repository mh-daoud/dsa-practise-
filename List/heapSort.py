# Heap sort is a comparison-based sorting technique based on Binary Heap data structure.
# It is similar to the selection sort where we first find the minimum element and place the minimum element at
# the beginning. Repeat the same process for the remaining elements.
# time complexity O(nLog(n)), space complexity O(1)

def heapify(arr, N, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < N and arr[largest] < arr[l]:
        largest = l
    if r < N and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        temp = arr[largest]
        arr[largest] = arr[i]
        arr[i] = temp
        heapify(arr, N, largest)
# nums = [3, 9, 13, 17, 21, 7, 5, 4, 2, 1, 3]


def heapSort(arr):
    N = len(arr)

    # create heap inplace
    for i in range(N//2 - 1, -1, -1):
        heapify(arr, N, i)
    # swap index 0 (max) with last element  and repeat
    for i in range(N-1, 0, -1):
        temp = arr[i]
        arr[i] = arr[0]
        arr[0] = temp
        heapify(arr, i, 0)


nums = [3, 9, 13, 2, 1, 7, 5, 4, 17, 21, 3]
print(nums)
heapSort(nums)
print(nums)
