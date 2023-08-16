# eq = 6k +- 1, stop condition n^0.5
# time O(N), space (O(K) where k is primal up to N)
import math


def findNPrimal(N):

    if N <= 1:
        return []
    if N % 2 == 0 or N % 3 == 0:
        return []
    results = [2, 3]
    for k in range(5, N, 6):
        if N % k != 0:
            results.append(k)
        if N % (k+2) != 0:
            results.append(k+2)
    return results


output = findNPrimal(23)
print(output)
