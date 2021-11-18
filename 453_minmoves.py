class Solution(object):
    def minMoves(self, nums):
        m = min(nums)
        moves = 0
        for num in nums:
            moves += (num - m)
        return  moves

A = [1, 3, 5, -3]
ans = Solution.minMoves(Solution,A)
print(ans)