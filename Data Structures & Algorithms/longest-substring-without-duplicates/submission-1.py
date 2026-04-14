class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stringSet = set()
        l = 0
        res = 0
        for r, char in enumerate(s):
            while char in stringSet:
                stringSet.remove(s[l])
                l += 1
            stringSet.add(char)
            res = max(res, r - l + 1)
        return res
