class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        ans = 0
        for i in range(0, len(timeSeries) - 1):
            diff = timeSeries[i+1] - timeSeries[i]
            ans += max(duration, diff)
        return ans