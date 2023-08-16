def avg(lst):
    sum = 0
    for temp in lst :
        sum += temp
    return sum / len(lst)

def countAboveLimit(limit, lst):
    count = 0
    for temp in lst:
        if temp > limit :
            count += 1
    return count

tempConut = input("please enter how many days temprture are there ? ")
temps = []

for dayTemp in range(0, int(tempConut)) : 
    temp = input("enter day " + str(dayTemp+1) + " temprture: ")
    temps.append(float(temp))

avgTemp = avg(temps)
count = countAboveLimit(avgTemp,temps)
print("Avg temp = " + str(avgTemp) + " and there are " + str(count) + " day(s) above avg temp")
