class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return  " ".join([item for item in s.split(" ") if item != ""][::-1])
        
        
A = "   the sky is blue"
print(Solution.reverseWords(Solution, A))