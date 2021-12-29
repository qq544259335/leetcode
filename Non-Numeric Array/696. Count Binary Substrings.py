class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        pos = 0
        res = 0
        last = 0
        while pos < len(s):
            curBin = s[pos]
            count = 0
            while (pos < len(s)) and (curBin == s[pos]):
                count += 1
                pos += 1
            res += min(last, count)
            last = count
        return res