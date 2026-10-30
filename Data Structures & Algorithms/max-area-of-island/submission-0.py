class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != 1:
                return 0
            else:
                grid[r][c] = 0

                left = dfs(r-1, c)
                right = dfs(r+1, c)
                down = dfs(r, c-1)
                up = dfs(r, c+1)

                return 1+left+right+up+down
        
        
        maxsize = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                
                area = dfs(i, j)
                maxsize = max(area, maxsize)

        return maxsize