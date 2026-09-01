class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        nums.sort()

        def backtrack(index, remain):
            if remain == 0:
                res.append(path.copy())
                return
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                if nums[i] > remain:
                    break

                path.append(nums[i])
                backtrack(i + 1, remain - nums[i])
                path.pop()

        backtrack(0, target)
        return res 