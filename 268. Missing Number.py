def missing_number(nums):
    """Finds the missing value in a [0,n] array"""
    nums.sort()
    for i, v in enumerate(nums):
        if i!=v:
            return i
    
    return len(nums)


nums = [0, 3, 4, 2]
print(missing_number(nums))