class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(1, len(s)):
            s.insert(0, s.pop(i))

A = ["h","e","l","l","o"]
Solution.reverseString(Solution, A)
print(A)