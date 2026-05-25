def find_disappeared_numbers(nums):
    set_nums = set(nums)
    
    res = []

    for i in range(1, len(nums)+1):
        if i not in set_nums:
            res.append(i)

    return res


nums = [1,1]

print(find_disappeared_numbers(nums))