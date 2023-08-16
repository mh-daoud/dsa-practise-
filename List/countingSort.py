# Counting sort is a sorting technique based on keys between a specific range.
# It works by counting the number of objects having distinct key values (a kind of hashing).
# Then do some arithmetic operations to calculate the position of each object in the output sequence.
# time , and space

def countingSort(arr):
    max = arr[0]
    for i in arr:
        if max <= i:
            max = i
    max += 1
    count = [0 for i in range(max)]

    output = [0 for i in range(len(arr))]

    for i in arr:
        count[i] += 1

    for i in range(1, max):
        count[i] += count[i - 1]

    for i in arr:
        count[i] -= 1
        output[count[i]] = i

    return output


nums = [3, 9, 13, 2, 1, 7, 5, 4, 17, 21, 3]
print(nums)
nums = countingSort(nums)
print(nums)
