class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A, B = 0, 0
        S, G = {}, {}
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                A += 1
            else:
                S[secret[i]] = S.get(secret[i], 0) + 1
                G[guess[i]] = G.get(guess[i], 0) + 1
        for key in S:
            if key in G:
                B += min(S[key], G[key])
        return "%sA%sB" % (A, B)     

S = "1123"
G = "0111"
print(Solution.getHint(Solution, S, G))