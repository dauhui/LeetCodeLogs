from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        groups = defaultdict(list)
        for w in strs:
            sor = "".join(sorted(w))
            groups[sor].append(w)
        return groups.values()

A = ["eat","tea","tan","ate","nat","bat"]
print(Solution.groupAnagrams(Solution, A))