import math

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        count = math.ceil(len(s)/(2* numRows - 2))
        res = ""
        print(count)
        for m in range(numRows):
            for k in range(count):
                start = k*(2*numRows - 2)
                if m == 0:
                    res += s[start]
                    continue
                pos1 = start + m
                pos2 = start +   (2*numRows - 2 -m)
                if pos1 == pos2:
                    if pos1 < len(s):
                        res += s[pos1]
                else:
                    if pos1 < len(s):
                        res += s[pos1]
                    if pos2 <len(s):
                        res += s[pos2]
        return res


string = "ab"
num = 2
sol = Solution()
print(sol.convert(string, num))