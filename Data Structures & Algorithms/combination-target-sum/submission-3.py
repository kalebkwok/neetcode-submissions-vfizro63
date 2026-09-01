class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        nums.sort()

        def backtrack(index, remain):
    
            if remain == 0:
                res.append(path.copy())
                return
            for i in range(index, len(nums)):
                if nums[i] > remain:
                    break
                path.append(nums[i])
                backtrack(i, remain - nums[i])
                path.pop()

        backtrack(0, target)
        return res 