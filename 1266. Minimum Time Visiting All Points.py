def minimum_time(points):
    res = 0

    for i in range(1, len(points)):
        x0, y0 = points[i-1]
        x1, y1 = points[i]

        value = max(abs(x1-x0), abs(y1-y0))
        res += value

    return res


nums = [[3,2],[-2,2]]

print(minimum_time(points=nums))