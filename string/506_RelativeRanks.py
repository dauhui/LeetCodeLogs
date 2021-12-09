class Solution:
    def findRelativeRanks(self, scores: List[int]) -> List[str]:
        rank = {}
        for i, val in enumerate(sorted(scores, reverse=True)):
            rank[val] = i + 1
        
        medal = {1: "Gold Medal", 2: "Silver Medal", 3:"Bronze Medal"}
        return [medal.get(rank[score], str(rank[score])) for score in scores]

