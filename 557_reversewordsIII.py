class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str

        --split with " "
        --pick ith element
        --list() the element
        --[::-1]

        """
        s = s.split(" ")
        for i in range(len(s)):
            s[i] = "".join(list(s[i])[::-1])
        return  " ".join(s)

A = "Let's take LeetCode contest"
print(Solution.reverseWords(Solution, A))