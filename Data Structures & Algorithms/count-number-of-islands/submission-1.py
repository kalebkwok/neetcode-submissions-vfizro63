class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        def bfs(i, j):
            q = deque()
            grid[i][j] = "0"
            q.append((i, j))

            while q:
                i, j = q.popleft()
                for dx, dy in [[0,1], [1,0], [0, -1], [-1, 0]]:
                    x, y = i + dx, j + dy
                    if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == "0":
                        continue
                    q.append((x, y))
                    grid[x][y] = "0"

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(i, j)
                    res += 1
        return res