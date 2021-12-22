class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack: return -1
        if needle == '': return 0
        return haystack.index(needle)