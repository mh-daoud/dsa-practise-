# Radix Sort is a linear sorting algorithm that sorts elements by processing them digit by digit.
# It is an efficient sorting algorithm for integers or strings with fixed-size keys.
# time , space


def radixSort(arr):
    max = arr[0]

    for i in arr:
        if max < i:
            max = i

    exp = 1
    while max / exp >= 1:
        arr = countingSort(arr, exp)
        exp *= 10
    return arr


def countingSort(arr, exp):
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)
    for i in arr:
        index = i // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i-1]

    for i in range(n-1, -1, -1):
        index = arr[i] // exp
        count[index % 10] -= 1
        output[count[index % 10]] = arr[i]

    return output


nums = [3, 9, 13, 2, 1, 7, 5, 4, 17, 21, 3]
print(nums)
nums = radixSort(nums)
print(nums)
