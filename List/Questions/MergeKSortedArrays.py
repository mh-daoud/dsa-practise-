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


def merge(nums1, nums2):
    output = []
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            output.append(nums1[i])
            i += 1
        else:
            output.append(nums2[j])
            j += 1
    while i < len(nums1):
        output.append(nums1[i])
        i += 1
    while j < len(nums2):
        output.append(nums2[j])
        j += 1
    return output


def split(nums, l, r):
    # 0 3 1, 0 1 0 , 2 3 2
    if l < r:
        m = l + ((r - l) // 2)
        print(l, r, m)
        nums1 = split(nums, l, m)  # 0,1 , 0,0 , 2,2
        nums2 = split(nums, m+1, r)  # 2,3 , 1,1 , 3,3
        return merge(nums1, nums2)
    return nums[r]


nums = [[2, 6, 12, 34],
        [1, 9, 20, 1000],
        [23, 34, 90, 2000]]
print(nums)
nums2 = split(nums, 0, len(nums)-1)
print(nums2)
