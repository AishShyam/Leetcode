def contains_duplicate(nums):
    """Checks if the array contains duplicate numbers by checking the length of the array and comparing with the length of set which do not allow for duplicates"""
    if len(set(nums)) == len(nums):
        return False
    else:
        return True
    

nums = [1,2,3]

print(contains_duplicate(nums))