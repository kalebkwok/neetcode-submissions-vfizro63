class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charList = [0] * 26
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            charList[ord(s[i]) - ord('a')] += 1
            charList[ord(t[i]) - ord('a')] -= 1
        
        for element in charList:
            if element != 0:
                return False
        
        return True