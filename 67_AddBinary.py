class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        11+1 -> 12 -> 20 -> 100
        11+11 -> 22 -> 30 -> 110
        """
        sum = list('0' + str(int(a)+int(b)))
        temp = 0
        cnt = 0
        for i in range(len(sum)-1,-1,-1):
            cnt += 1
            sum[i] = str(int(sum[i]) + temp)
            if int(sum[i]) > 1:
                sum[i] = str(int(sum[i])%2)
                temp = 1
            else:
                temp = 0
        if sum[0] == '0': sum.pop(0)
        return ''.join(sum)
        
a = '1'
b = '10'
print(Solution.addBinary(Solution, a, b))