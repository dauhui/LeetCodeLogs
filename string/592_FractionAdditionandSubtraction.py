import re
class Solution:
    def fractionAddition(self, expression: str) -> str:
        
        def getGCD(a, b):
            while b: a, b = b, a%b
            return a

        nums = re.findall('[+-]?\d+', expression)
        nominators, denominators = [], []
        
        for i in range(len(nums)//2):
            nominators.append(int(nums[2*i]))
            denominators.append(int(nums[2*i+1]))
            
        LCM, GCD = 1, 1
        for denominator in denominators:
            GCD = getGCD(GCD, denominator)
            LCM = LCM*denominator // GCD
        
        N = 0
        for n, d in zip(nominators, denominators):
            N += n * LCM // d
            
        GCD = getGCD(N, LCM)
        return "{}/{}".format(N//GCD, LCM//GCD)

