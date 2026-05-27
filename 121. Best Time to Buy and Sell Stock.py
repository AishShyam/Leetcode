def bestTime(prices):
    i = 0
    j = i + 1
    res = 0

    while i < j and j < len(prices):
        if prices[i] < prices[j]:
            value = prices[j] - prices[i]
            res = max(res, value)

        else:
            i = j
        j+=1

    return res

prices = [7,6,4,3,1]

print(bestTime(prices))