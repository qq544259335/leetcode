class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        res_int = num
        while len(s) != 1:
            res_int = 0
            for c in s:
                res_int += int(c)
            s = str(res_int)
        return res_int

test = Solution()
print(test.addDigits(938))

