class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:    
        minutes = []
        for timePoint in timePoints:
            minutes.append(int(timePoint[:2])*60 + int(timePoint[3:]))
            
        minutes.sort()
        return min((minutes[i] - minutes[i-1]) % (60*24) for i in range(len(minutes)))

