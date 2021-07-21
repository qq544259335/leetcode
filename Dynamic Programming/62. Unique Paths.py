class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for i in range(m):
            if i == 0:
                dp.append([1] * n)
            else:
                dp.append([0] * n)
                dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    def uniquePaths2(self, m: int, n: int) -> int:
        pre = [1] * n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                    cur[j] = cur[j - 1] + pre[j]
            pre = cur[:]
        return pre[-1]

    def uniquePaths3(self, m: int, n: int) -> int:
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                    cur[j] = cur[j - 1] + cur[j]
        return cur[-1]

    def uniquePath20210622(self, m: int, n: int) -> int:
        res = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                res[j] += res[j - 1]
        return res[-1]

solve = Solution()
print(solve.uniquePath20210622(3,7))