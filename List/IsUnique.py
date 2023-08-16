from operator import truediv


def frequencyArray(lst):
    eArray = []
    vistied = -1
    for element in lst:
        eArray.append(0)
    
    for i in range(0,len(lst)):
        count = 1
        for j in range(i + 1 ,len(lst)):
            if lst[i] == lst[j] :
                count +=1
                eArray[j] = vistied
        if eArray[i] != vistied :
            eArray[i] = count
           
    return eArray

def isUinque(lst) :
    freq = frequencyArray(lst)
    for num in freq :
        if num > 1 :
            return False
    return True

lst = [1,2,3,4,2,5,1,6,1,7,2,8,9,10,1,15,77,1,90,2,5,33,20,3,44,2,15,26,1,7,39]
lst2 = [1,2,3,4,5,6,7,8,9]
freq = isUinque(lst2)
print(freq)






# create empty array of same length as orignal array (a) call it (eArray)
# loop throguh original array (i) from 0 to length and do
#   1- let count = 1
#   2- loop throguh the (j) orignal array from i+1 to length again and check if a[i] == a[j] if so increase count++ and mark  list as visited
# after the loop check if the i elelment in the new array not visted set eArray[i] = count