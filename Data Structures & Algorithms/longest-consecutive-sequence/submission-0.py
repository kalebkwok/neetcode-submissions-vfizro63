class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        res = 0

        for element in numsSet:
            
            if element - 1 not in numsSet:
                temp = 1
                while element +1 in numsSet:
                    temp += 1
                    element += 1
                res = max(temp, res) 

        return res