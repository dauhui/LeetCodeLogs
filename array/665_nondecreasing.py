class Solution(object):
    def checkPossibility(self, nums):
        cnt = 0
        nums.insert(0, -10e5 - 1)
        for i in range(len(nums) - 2):
            if (nums[i+1] - nums[i])*(nums[i+2] - nums[i+1]) < 0:
                nums.pop(i + 1)
                break
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return  False
        return True

A = [5,7,1,8]
ans = Solution.checkPossibility(Solution,A)
print(ans)