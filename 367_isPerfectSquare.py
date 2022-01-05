class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True # edge case
        l, r = 1, num
        while r - l > 1:
            mid = l + (r - l)//2
            if num == pow(mid,2):
                return True
            elif num < pow(mid,2):
                r = mid
            elif num > pow(mid,2):
                l = mid
        return False
        
num = 256
print(Solution.isPerfectSquare(Solution, num))