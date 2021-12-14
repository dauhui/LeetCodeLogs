class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        for i in range(1, len(score) + 1):
            score[score.index(max(score))] = -i
        for i in range(len(score)):
            if score[i] == -1:
                score[i] = "Gold Medal"
            elif score[i] == -2:
                score[i] = "Silver Medal"
            elif score[i] == -3:
                score[i] = "Bronze Medal"
            else:
                score[i] = str(score[i]*-1)
        return score

A = [10, 3, 8, 9, 4]
print(Solution.findRelativeRanks(Solution, A))