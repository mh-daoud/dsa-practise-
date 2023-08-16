# def: insertion sort is a simple sorting algorithm with O(n^2) time complexity, and O(1) space complexity
# concept: the array is virtually split into sorted and unsorted parts,
# Values from the unsorted part are picked and placed at the correct position in the sorted part.

def insertionSort(arr):

    for i in range(1, len(arr)):

        key = arr[i]
        j = i - 1
        # move elements that are greater than key one position after their current position
        # to make space for the key to take it place
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


nums = [1, 5, 3, 8, 13, 6, 7, 2]

print(nums)
insertionSort(nums)
print(nums)
