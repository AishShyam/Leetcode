def smaller_than_current(nums):
    d = {}

    res = []

    sorted_nums = sorted(nums)

    for i, v in enumerate(sorted_nums):
        if v not in d:
            d[v] = i

    for num in nums:
        res.append(d[num])

    return res

nums = [8,1,2,2,3]

print(smaller_than_current(nums=nums))
