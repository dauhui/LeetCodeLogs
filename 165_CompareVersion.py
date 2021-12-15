class Solution(object):
    def compareVersion(self, v1, v2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # v1 = v1.replace('.','')
        # v2 = v2.replace('.','')
        # for i in range(abs(len(v1)-len(v2))):
        #     if len(v1) > len(v2):
        #         v2 += '0'
        #     elif len(v1) < len(v2):
        #         v1 += '0'
        # if int(v1) > int (v2):
        #     return 0
        # return -1
        v1 = v1.split('.')
        v2 = v2.split('.')
        for i in range(abs(len(v1)-len(v2))):
            if len(v1) > len(v2):
                v2.append('0')
            elif len(v1) < len(v2):
                v1.append('0')
        for i in range(len(v1)):
            if int(v1[i]) > int(v2[i]):
                return 1
            if int(v1[i]) < int(v2[i]):
                return -1
        return 0
version1 = "1.01"
version2 = "1.001"
print(Solution.compareVersion(Solution,version1,version2))