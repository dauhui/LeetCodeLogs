class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # reference from discussion
        k = k%len(nums)

        for i in range(k):
            p = nums.pop()
            nums.insert(0, p)



A = [1,2,3,4,5,6,7]
ans = Solution.rotate(Solution, A, 3)
print(ans)