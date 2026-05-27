def squaresOfSortedArray(nums):
    n = len(nums)
    i = 0
    j = n - 1
    pos = n - 1
    res = [0] * n

    while i<=j:
        if abs(nums[i]) > abs(nums[j]):
            res[pos] = nums[i] * nums[i]
            pos -= 1
            i += 1
        else:
            res[pos] = nums[j] * nums[j]
            pos -= 1
            j -= 1
        
    return res

nums = [-7,-3,2,3,11]

print(squaresOfSortedArray(nums))