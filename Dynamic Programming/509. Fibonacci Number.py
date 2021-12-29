class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        pp = 0
        p = 1
        for i in range(2, n + 1):
            cur = p + pp
            p, pp = cur, p
        return cur


test = Solution()
print(test.fib(3))
