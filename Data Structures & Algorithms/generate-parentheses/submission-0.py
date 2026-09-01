class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        res = []

        def backtrack(left, right):
            if left == right == n:
                res.append("".join(path))
                return
            if left < n:
                path.append("(")
                backtrack(left + 1, right)
                path.pop()
            if right < left:
                path.append(")")
                backtrack(left, right + 1)
                path.pop()

        backtrack(0, 0)

        return res