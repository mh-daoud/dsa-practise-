"""
Given K sorted arrays of size N each, merge them and print the sorted output.

Examples:

Input: K = 3, N = 4, arr = { {1, 3, 5, 7}, {2, 4, 6, 8}, {0, 9, 10, 11}}
Output: 0 1 2 3 4 5 6 7 8 9 10 11 
Explanation: The output array is a sorted array that contains all the elements of the input matrix. 

Input: k = 4, n = 4, arr = { {1, 5, 6, 8}, {2, 4, 10, 12}, {3, 7, 9, 11}, {13, 14, 15, 16}} 
Output: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
Explanation: The output array is a sorted array that contains all the elements of the input matrix. 
"""


def leftNode(i):
    return 2 * i + 1


def rightNode(i):
    return 2 * i + 2


def isLeafNode(i, N):
    if i < N-1 and i > (N-1)//2:
        return True
    return False


def parentNode(i):
    return (i - 1) // 2


def addToHeap(output, arr, i):
    output.append(arr[i])
    N = len(output) - 1
    while N != 0 and output[N] > output[parentNode(N)]:
        swap(output, N, parentNode(N))
        N = parentNode(N)


def swap(arr, i, n):
    temp = arr[i]
    arr[i] = arr[n]
    arr[n] = temp


def heapify(arr, i, N):
    l = leftNode(i)
    r = rightNode(i)
    largest = i
    if l < N and arr[largest] < arr[l]:
        largest = l
    if r < N and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        swap(arr, largest, i)
        heapify(arr, largest, N)


def sort(nums):
    output = []
    for arr in nums:
        for i in range(len(arr)):
            addToHeap(output, arr, i)
    N = len(output)
    for j in range(N-1, 0, -1):
        swap(output, 0, j)
        heapify(output, 0, j)
    return output


def getTree(arr, i):
    if i < len(arr):
        l = leftNode(i)
        r = rightNode(i)
        result = "" + str(arr[i]) + " -> "
        if l < len(arr):
            result += str(arr[l])
        if r < len(arr):
            result += " - " + str(arr[r])
        return result
    return ""


nums = [[2, 6, 12, 34],
        [1, 9, 20, 1000],
        [23, 34, 90, 2000]]

result = sort(nums)
print(result)
