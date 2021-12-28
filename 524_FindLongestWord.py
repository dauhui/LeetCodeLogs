class Solution(object):
    def findLongestWord(self, s, dictionary):

        def isSubstring(s, t):
            s = list(s)
            t = list(t)
            while len(s) > 0 and len(t) > 0:
                if s[-1] == t[-1]:
                    s.pop()
                    t.pop()
                else:
                    s.pop()
            return len(t) == 0

        dictionary = sorted(dictionary, key=lambda x: (-len(x), x))
        for item in dictionary:
            if isSubstring(s, item):
                return item
        return ""

s = "abpcplea"
dictionary = ["a", "b", "c"]
print(Solution.findLongestWord(Solution, s, dictionary))