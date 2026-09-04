class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        max_res = 0

        m, n = len(grid), len(grid[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        def dfs(i, j):
            nonlocal res
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return
            res += 1
            grid[i][j] = 0
            for di, dj in directions:
                dfs(i + di, j + dj)


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = 0
                    dfs(i, j)
                    max_res = max(res, max_res)

        return max_res