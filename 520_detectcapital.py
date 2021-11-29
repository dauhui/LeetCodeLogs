class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cnt1, cnt2 = 0, 0
        for i in range(1, len(word)):
            if word[i].isupper():
                cnt1 += 1
            else:
                cnt2 += 1
            if cnt1 > 0 and cnt2 > 0:
                return  False
        if word[0].isupper() == False and cnt1>0:
            return  False
        return  True
