class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                index = ord(char) - ord("a")
                count[index] += 1
            key = tuple(count)
            res[key].append(word)
        return list(res.values())