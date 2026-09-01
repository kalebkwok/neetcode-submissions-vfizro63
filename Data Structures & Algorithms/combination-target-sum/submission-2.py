class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        nums.sort()

        def backtrack(index, remain):
            if remain < 0:
                return 
        
            if remain == 0:
                res.append(path.copy())

            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i, remain - nums[i])
                path.pop()

        backtrack(0, target)
        return res 