class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        table = {}
        output = []
        for chr in s:
            if chr in table:
                table[chr] += 1
            else:
                table[chr] = 1
        table = sorted(table.items(), key=lambda item: item[1], reverse=True)
        for k, v in table:
            for i in range(v):
                output.append(k)
        return "".join(output)

A = "treeE"
print(Solution.frequencySort(Solution, A))