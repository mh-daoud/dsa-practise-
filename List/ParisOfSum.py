def findPairs(lst, target):
    start = 0
    length = len(lst)
    while start < length :
        for index in range(start,length):
            if (lst[start] + lst[index]) == target:
                return print("indcies of paris that add to " + str(target) + " are (" + str(start) + "," + str(index) + ")")
        start += 1
    return print("no indcies found")

lst = [3,4,5,11,17,21,4]
target = int(input("please enter a target ? "))

findPairs(lst,target)

# [1,2,3,4,5] 
# start = 0
# loop index from start til end
    # if start + index = target 
    # return (start,index)
    # index++
# start += 1, if start < length repeat else error