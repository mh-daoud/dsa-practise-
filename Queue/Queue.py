from collections import deque

numbers = deque()


def setupQueue(nums):
    for num in nums:
        numbers.append(num)


setupQueue([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(numbers.popleft())
print(numbers.popleft())
