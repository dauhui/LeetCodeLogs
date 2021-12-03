class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for cha in ransomNote:
            if cha in magazine:
                magazine = magazine.replace(cha,"",1)
            else:
                return False
        return True

A = "aa"
B = "aab"
print(Solution.canConstruct(Solution, A, B))