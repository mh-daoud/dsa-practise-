def zeroOneKnapsack(items,maxC):
    maxSum = 0
    for excludedIndex in range(-1,len(items)):
       maxSum = magicFunction(excludedIndex,items,maxC,maxSum)
    return maxSum

def magicFunction(excludedIndex,items,maxC,maxSum):
    i = 0
    c = 0
    sum = 0
    while c < maxC:
        if i == len(items):
            break
        if excludedIndex != i and c + items[i].weight <= maxC:
           sum += items[i].value
           c += items[i].weight 
        i+= 1
    return max(maxSum,sum)

class Item :
    def __init__(self,weight,value):
        self.weight = weight
        self.value = value


items = [
    Item(10,1),
Item(5,10),
Item(5,7),
Item(1,1),
Item(3,10),
Item(7,4),
Item(8,14),
]

items2 = [
   Item(5,1),
Item(5,10),
Item(5,7), 
]

maxC = 15

print(zeroOneKnapsack(items,maxC))