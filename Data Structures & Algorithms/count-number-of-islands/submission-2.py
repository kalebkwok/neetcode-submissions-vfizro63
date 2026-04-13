class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False 
        if self.size[pu]> self.size[pv]:
            self.size[pu] += self.size[pv]
            self.parent[pv] = pu
        else:
            self.size[pv] += self.size[pu]
            self.parent[pu] = pv
        return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        dsu = DSU(m * n)

        def index(i, j):
            return i * n + j
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    for dx, dy in [[0,1],[1,0],[0, -1],[-1, 0]]:
                        x, y = i + dx, j + dy
                        if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == "0":
                            continue
                        if dsu.union(index(i, j), index(x, y)):
                            res -= 1
    
        return res


        