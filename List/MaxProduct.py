def maxProduct(lst):
    product = -1
    for lowIndex in range(0,len(lst)):
        for nextIndex in range(lowIndex+1, len(lst)):
            if product < lst[lowIndex] * lst[nextIndex] :
                product = lst[lowIndex] * lst[nextIndex]
                pairs = str(lowIndex) + "," + str(nextIndex)
    print(product)
    print(pairs)


lst = [45,6,79,12,81,33,4,39,28,47,32,14,26,47,33,29,30,20,43,56]

maxProduct(lst)

