class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        number_count = [0] * 10
        s_num = str(num)
        for c in s_num:
            if c == '-':
                continue
            number_count[int(c)] += 1
        if num > 0:
            i = 1
            while number_count[i] == 0:
                i += 1
            res = str(i)
            number_count[i] -= 1
            for i in range(len(number_count)):
                res += number_count[i] * str(i)
            return int(res)
        else:
            res = ""
            for i in range(9, - 1, - 1):
                res += number_count[i] * str(i)
            return -int(res)


test = Solution()
print(test.smallestNumber(-6709))
