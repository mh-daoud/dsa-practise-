def zeroOneKnapsack(items,capacity,currentIndex):
    if capacity <= 0 or currentIndex >= len(items):
        return 0
    elif capacity >= items[currentIndex].weight :
        profit1 = items[currentIndex].value + zeroOneKnapsack(items,capacity - items[currentIndex].weight,currentIndex+1)
        profit2 = zeroOneKnapsack(items,capacity,currentIndex+1)
        return max(profit1,profit2)
    else :
        return 0


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

print(zeroOneKnapsack(items2,maxC,0))