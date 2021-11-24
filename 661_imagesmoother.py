import copy
class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        x_len = len(img)
        y_len = len(img[0])
        cimg = copy.deepcopy(img)

        for x in range(x_len):
            for y in range(y_len):
                neighbor = [
                    img[i][j]
                    for i in (x-1, x, x+1)
                    for j in (y-1, y, y+1)
                    if 0 <= i < x_len and 0 <= j < y_len
                ]
                cimg[x][y] = sum(neighbor) // len(neighbor)

        return cimg

A = [[100,200,100],[200,50,200],[100,200,100]]
ans = Solution.imageSmoother(Solution, A)
print(ans)