class Solution(object):
    def moveZeroes(self, nums):
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == 0:
               cnt += 1
        for i in range(cnt):
            nums.remove(0)
            nums.append(0)
        return  nums

A = [0]
ans = Solution.moveZeroes(Solution,A)
print(ans)