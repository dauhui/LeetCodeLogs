class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        """calculate the total time of poison"""
        total = 0
        for i in range(0, len(timeSeries) - 1):
            maxRange = timeSeries[i+1] - timeSeries[i]
            ans += min(duration, maxRange)
        return ans + duration
