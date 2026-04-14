class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charDict = {}
        res = 0

        l = 0
        maxf = 0
        for r, char in enumerate(s):
            charDict[char] = 1 + charDict.get(char, 0)
            maxf = max(maxf, charDict[char])

            while (r - l + 1) - maxf > k:
                charDict[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res 