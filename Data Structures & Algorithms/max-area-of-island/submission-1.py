class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxArea = 0

        def dfs(i, j):
            if i >= m or j >= n or i < 0 or j < 0 or grid[i][j] == 0:  
                return 0
            grid[i][j] = 0
            area = 1
            
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                area += dfs(i + dx, j + dy)
            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
        
        return maxArea