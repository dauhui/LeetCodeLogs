def isBadVersion(version):
    bad = 4
    if version == bad:
        return True
    else:
        return False

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        if isBadVersion(l):
            return l
        while (r - l) > 1:
            mid = l + (r - l)//2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid
        return r



n = 5
print(Solution.firstBadVersion(Solution, n))