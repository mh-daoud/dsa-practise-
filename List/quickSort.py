# QuickSort is a sorting algorithm based on the Divide and Conquer algorithm
# that picks an element as a pivot and partitions the given array around the picked pivot
# by placing the pivot in its correct position in the sorted array.
# time complexity O(n^2) , space complexity O(log(n))

def swap(arr, first, second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp


def partition(arr, low, high):
    i = low
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            swap(arr, j, i)
            i += 1
    swap(arr, i, high)
    return i


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


nums = [3, 9, 13, 2, 1, 7, 5, 4, 17, 21, 3]
print(nums)
quickSort(nums, 0, len(nums)-1)
print(nums)
