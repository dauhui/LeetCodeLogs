class Solution:
    def mySqrt(self, num: int) -> int:
        if num == 0: return 0 # edge case
        l, r = 1, num
        while r - l > 1:
            mid = l + (r - l)//2
            if num == pow(mid,2):
                return mid
            elif num < pow(mid,2):
                r = mid
            elif num > pow(mid,2):
                l = mid
        return l
        
num = 1
print(Solution.mySqrt(Solution, num))