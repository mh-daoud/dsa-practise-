def primal(N):
    output = []
    nums = [True] * (N+1)

    p = 2

    while p * p < N+1:
        if nums[p]:
            for k in range(p*p, N, p):
                nums[k] = False
        p += 1
    for i in range(2, len(nums)):
        if nums[i]:
            output.append(i)
    print(nums)
    return output


nums = primal(23)
print(nums)
