def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


fact4 = factorial(2)
print(fact4)
