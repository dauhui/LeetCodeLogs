class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        I 1
        V 5
        X 10
        L 50
        C 100
        D 500
        X 1000
        """
        s = list(s)
        s = [1 if i=='I' else 5 if i=='V' else 10 if i=='X' else 50 if i=='L' else 100 if i=='C' else 500 if i =='D' else 1000 for i in s]
        s = s[::-1]
        s.insert(0,0)
        res = s[0]
        for i in range(len(s)-1):
            if s[i] <= s[i+1]:
                res += s[i+1]
            else:
                res -= s[i+1]
        return res
        
A = "MCMXCIV"
print(Solution.romanToInt(Solution, A))