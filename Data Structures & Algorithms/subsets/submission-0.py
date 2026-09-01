class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []

        def backtrack(start):
            res.append(path.copy())
            for j in range(start, len(nums)):
                path.append(nums[j])
                backtrack(j + 1)
                path.pop()

        backtrack(0)
        return res