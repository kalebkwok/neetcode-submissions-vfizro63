class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for element in strs:
            key = tuple(sorted(element))
            res[key].append(element)
        
        return list(res.values())