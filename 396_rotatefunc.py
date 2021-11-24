class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        multi = [i for i in range(len(nums))]
        for i in range(len(nums)):
            ans = max(ans, sum(nums[i]*multi[i] for i in range(len(nums))))
            p = nums.pop(0)
            nums.append(p)
        return  ans

A = [4,3,2,6]
ans = Solution.maxRotateFunction(Solution, A)
print(ans)