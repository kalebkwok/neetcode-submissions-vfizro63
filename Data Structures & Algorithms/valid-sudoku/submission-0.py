class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        set1 = defaultdict(set)
        set2 = defaultdict(set)
        set3 = defaultdict(set)

        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    continue
                c = board[i][j]
                if c in set1[i] or c in set2[j] or c in set3[(i//3, j//3)]:
                    return False
                set1[i].add(c)
                set2[j].add(c)
                set3[(i//3, j//3)].add(c)
        return True
                