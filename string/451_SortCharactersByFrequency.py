class Solution:
    def frequencySort(self, s: str) -> str:
        
        count = list(Counter(s).items())
        count.sort(key=lambda x: -x[1])
        
        res = ""
        for key, val in count:
            res += key*val
        
        return res

