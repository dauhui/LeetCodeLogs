class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_sum, t_sum = 0, 0
        for cha in s:
            s_sum += ord(cha)
        for cha in t:
            t_sum += ord(cha)
        return  chr(t_sum - s_sum)

A = ""
B = "y"
print(Solution.findTheDifference(Solution, A, B))