def mergeSort(arr, l, r):
    if l < r:
        m = l + ((r-l)//2)
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    print('l =' + str(l) + ', r = ' + str(r)+', m = ' +
          str(m) + ', n1 =' + str(n1) + ', n2=' + str(n2))

    L = []
    R = []
    i = j = 0
    k = l

    while i < n1:
        L.append(arr[l + i])
        i += 1
    while j < n2:
        R.append(arr[m+j+1])
        j += 1

    i = 0
    j = 0

    while i < n1 and j < n2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


nums = [3, 9, 13, 2, 1, 7, 5, 4, 17, 21, 3]
print(nums)
mergeSort(nums, 0, len(nums)-1)
print(nums)
