class Solution(object):
    A = [1,2,2,3,1,4,2]
    first, count, res, degree = {}, {}, 0, 0
    for i, a in enumerate(A):
        first.setdefault(a, i)
        count[a] = count.get(a, 0) + 1
        if count[a] > degree:
            degree = count[a]
            res = i - first[a] + 1
        elif count[a] == degree:
            res = min(res, i - first[a] + 1)
    print(res)