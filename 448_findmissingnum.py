class Solution(object):
    def findDisappearedNumbers(self, nums):
        # 下面這個運算時間過長
        # cnt = max(max(nums), len(nums))
        # ans = []
        # for i in range(1, cnt + 1):
        #     if i not in nums:
        #         ans.append(i)
        # return ans

        cnt = max(max(nums), len(nums))
        set_d = set(range(1, cnt+1)) - set(nums)
        return  list(set_d)