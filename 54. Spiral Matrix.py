def spiral_matrix(matrix):
    r1 = 0
    r2 = len(matrix) - 1
    c1 = 0
    c2 = len(matrix[0]) - 1

    res = []

    while r1<=r2 and c1<=c2:
        for i in range(c1, c2+1):
            res.append(matrix[r1][i])
        r1+=1

        for i in range(r1, r2+1):
            res.append(matrix[i][c2])
        c2-=1

        if r1<=r2:
            for i in range(c2, c1-1, -1):
                res.append(matrix[r2][i])
            r2-=1

        if c1<=c2:
            for i in range(r2, r1-1, -1):
                res.append(matrix[i][c1])
            c1+=1

    return res


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

print(spiral_matrix(matrix=matrix))