class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        visit = set()
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visit.add((i, j))
        def bfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or (i , j) in visit or grid[i][j] == -1:
                return
            visit.add((i, j))
            q.append((i, j))

        dist = 0
        while q:
            for i in range(len(q)):
                i, j = q.popleft()
                grid[i][j] = dist
                for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    bfs(i + dx, j + dy)
            dist += 1
