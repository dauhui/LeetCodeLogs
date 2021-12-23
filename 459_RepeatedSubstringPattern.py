class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        S = (s + s)[1:-1]
        return s in S

s = 'abcabc'
print(Solution.repeatedSubstringPattern(Solution, s))