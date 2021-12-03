from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """return true if ransomNote can be constructed from magazine and false otherwise"""
        count = Counter(magazine)
        for c in ransomNote:
            if not count.get(c): 
                return False
            else:
                count[c] -= 1
        return True

