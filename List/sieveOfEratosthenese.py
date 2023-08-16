def findPrimal(n):
    prime = [True] * (n+1)
    result = []

    p = 2
    while p * p <= n:  # O^0.5

        if prime[p] == True:
            for i in range(p*p, n + 1, p):  # 10,2,4,6,8 , #10,3,6,9 # 10,5
                prime[i] = False
        p += 1
    for i in range(2, n+1):  # N-1
        if prime[i]:
            result.append(i)
    return result


primes = findPrimal(120)
print(primes)
