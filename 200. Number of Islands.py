class Solution(object):

    def numOfIslands(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        res = 0
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    res += 1
        
        return res

    def dfs(self, grid, i, j):
        if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0'):
            return 
        
        grid[i][j] = '0'
        
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j-1)



grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


print(Solution().numOfIslands(grid=grid))

