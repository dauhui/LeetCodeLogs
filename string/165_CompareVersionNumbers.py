import re
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """
        - ignoring leading zeros
        
        ["0", "1", "1"] -> [1,1]
        ["1", "1"] -> [0,1]
        """
        
        v1 = list(map(int, re.findall(r'[.]?(\d+)', version1)))
        v2 = list(map(int, re.findall(r'[.]?(\d+)', version2)))
        
        for i in range(min(len(v1), len(v2))):
            if v1[i] > v2[i]: return 1
            if v1[i] < v2[i]: return -1
        
        if len(v1) > len(v2): return 1 if sum(v1[i+1:]) else 0
        if len(v1) < len(v2): return -1 if sum(v2[i+1:]) else 0

        return 0

