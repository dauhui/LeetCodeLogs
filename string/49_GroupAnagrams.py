class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def encode(string):
            res = [0]*26
            for c in string:
                res[ord(c) - ord("a")] += 1
            return tuple(res)
        
        group = {}
        for string in strs:
            code = encode(string)
            group[code] = group.get(code, []) + [string]
        
        return group.values()

