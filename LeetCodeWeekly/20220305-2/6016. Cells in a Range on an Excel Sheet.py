class Solution:
    def cellsInRange(self, s: str) -> [str]:
        c1, r1, c2, r2 = s[0], int(s[1]), s[-2], int(s[-1])
        res = []
        for i in range(ord(c2) - ord(c1) + 1):
            for j in range(r2 - r1 + 1):
                res.append(chr(ord(c1)+i) + str(r1 + j))
        return res