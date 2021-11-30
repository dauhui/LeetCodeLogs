class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len([item for item in s.split(' ') if item != ''][-1])

A = "   fly me  to  the moon     "
print(Solution.lengthOfLastWord(Solution, A))