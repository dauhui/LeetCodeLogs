class Solution(object):
    def originalDigits(self, s):
        """
        if is g, u, w, x, z:
            is 8, 4, 2, 6, 0
        if is f, h, o, s:
            is 5, 3, 1, 7
        if is i:
            is 9
        """
        table = {"g":0,"u":0,"w":0,"x":0,"z":0,"f":0,"h":0,"o":0,"s":0,"i":0}
        res = ""
        for cha in s:
            if cha in table:
                table[cha] += 1
        res += "0"*table["z"]
        res += "1"*(table["o"]-table["u"]-table["w"]-table["z"])
        res += "2"*table["w"]
        res += "3"*(table["h"]-table["g"]-table["u"]-table["w"]-table["z"])
        res += "4"*table["u"]
        res += "5"*(table["f"]-table["g"]-table["x"]-table["z"])
        res += "6"*table["x"]
        res += "7"*(table["s"]-table["g"]-table["x"]-table["z"])
        res += "8"*table["g"]
        res += "9"*(table["i"]-table["g"]-table["x"]-table["z"]-table["f"]-table["h"]-table["o"]-table["s"])
        return res

A = "owoztneoer"
print(Solution.originalDigits(Solution, A))