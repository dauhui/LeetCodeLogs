class Solution:
    def singleNonDuplicate(self, nums) -> int:
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        target = list(dict.keys())[list(dict.values()).index(1)]

        # lo, hi = 0, len(nums)
        # while lo < hi:
        #     mid = lo + (hi - lo) // 2
        #     if nums[mid] >= target:
        #         hi = mid
        #     else:
        #         lo = mid + 1

        return target


nums = [1,1,2,2,3,4,4]
print(Solution.singleNonDuplicate(Solution, nums))