def two_sum(target, nums):
    d = {}

    for i,v in enumerate(nums):
        complement = target - nums[i]
        if complement not in d:
            d[nums[i]] = i
        
        else:
            return [d[complement], i]
        
    return [-1,-1]


nums = [2,7,11,15]
target = 9
print(two_sum(target, nums))