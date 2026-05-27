def twoSumTwo(numbers, target):
    i = 0 
    j = len(numbers) - 1

    while(i<j):
        if numbers[i] + numbers[j] == target:
            return [i+1, j+1]
        elif numbers[i] + numbers[j] < target:
            i+=1
        else:
            j-=1

    return [-1, -1]


numbers = [2,3,4]
target = 6

print(twoSumTwo(numbers, target))