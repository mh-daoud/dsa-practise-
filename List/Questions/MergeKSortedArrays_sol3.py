import sys


class HeapNode:
    element = 0
    arrIndex = 0
    nextIndex = 0

    def __init__(self, element, arrIndex, nextIndex):
        self.element = element
        self.arrIndex = arrIndex
        self.nextIndex = nextIndex

    def __repr__(self):
        return str(self.element)


class MinHeap:
    size = 0
    arr = []

    def __init__(self, arr):
        self.size = len(arr)
        self.arr = arr
        i = (self.size // 2) - 1
        while i >= 0: # K/2
            self.minifyHeap(i) #/Log(K/2)
            i -= 1

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def swap(self, i, n):
        temp = self.arr[i]
        self.arr[i] = self.arr[n]
        self.arr[n] = temp

    def replaceRoot(self, element):
        self.arr[0] = element
        self.minifyHeap(0)

    def getRoot(self):
        return self.arr[0]

    def minifyHeap(self, i):
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if l < self.size and self.arr[l].element < self.arr[smallest].element:
            smallest = l
        if r < self.size and self.arr[r].element < self.arr[smallest].element:
            smallest = r
        if i != smallest:
            self.swap(i, smallest)
            self.minifyHeap(smallest)


def sortKSortedArrays(arrays):
    K = len(arrays) #1
    output = [] # 1
    resultSize = 0 # 1
    hArr = [] # 1

    for i in range(K): #K
        node = HeapNode(arrays[i][0], i, 1) #1
        resultSize += len(arrays[i]) #1
        hArr.append(node) # 1
    heap = MinHeap(hArr) #k2/4

    for i in range(resultSize): #N
        minNode = heap.getRoot() #1
        output.append(minNode.element) #1
        if minNode.nextIndex < len(arrays[minNode.arrIndex]):
            minNode.element = arrays[minNode.arrIndex][minNode.nextIndex]
            minNode.nextIndex += 1
        else:
            minNode.element = sys.maxsize
        heap.replaceRoot(minNode) #logk

    return (output)


nums = [[2, 6, 12, 34],
        [1, 9, 20, 1000],
        [23, 34, 90, 2000]]

output = sortKSortedArrays(nums)

print(output)
