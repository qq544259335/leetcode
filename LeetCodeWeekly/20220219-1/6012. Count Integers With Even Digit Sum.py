class Solution:
    def countEven(self, num: int) -> int:
        res = 0
        for i in range(1, num + 1):
            num = i
            temp = 0
            while num // 10 >= 1:
                temp += num % 10
                num = num // 10
            temp += num
            if temp % 2 == 0:
                res += 1
                print(i)
        return res
