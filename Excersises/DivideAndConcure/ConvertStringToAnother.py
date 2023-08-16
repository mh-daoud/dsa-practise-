def findOperationsCount(s1,s2):
    s1Length = len(s1)
    s2Length = len(s2)
    operationsCount = abs(s1Length - s2Length)
    for i in range(min(s1Length,s2Length)):
        if s1[i] != s2[i]:
            operationsCount += 1
    return operationsCount

print(findOperationsCount('table','tbrles'))