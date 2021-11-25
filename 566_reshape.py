class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        temp = []
        output = []
        for i in range(len(mat)):
            temp += mat[i]
        for i in range(r):
            output.insert(i, temp[0:4])
            del temp[0:4]
        return  output

A = [[1,2],[3,4]]
ans = Solution.matrixReshape(Solution, A, 1, 4)
print(ans)