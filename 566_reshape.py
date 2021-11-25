class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r*c != len(mat)*len(mat[0]):
            return  mat
        temp = []
        output = []
        for i in range(len(mat)):
            temp += mat[i]
        for i in range(r):
            output.insert(i, temp[0:c])
            del temp[0:c]
        return  output

A = [[1,2]]
ans = Solution.matrixReshape(Solution, A, 1, 4)
print(ans)