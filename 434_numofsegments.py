class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return  len([item for item in s.split(" ") if item != ""])
        
A = "my name    "
print(Solution.countSegments(Solution, A))