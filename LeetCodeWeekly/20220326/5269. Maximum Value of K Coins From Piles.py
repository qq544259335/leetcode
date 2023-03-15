class Solution:
    def maxValueOfCoins(self, piles: [[int]], k: int) -> int:
        # dp = [[-1] * (k + 1) for _ in range(len(piles) + 1)]
        #
        # def dpf(i, j):
        #     if dp[i][j] != -1:
        #         return dp[i][j]
        #     if i == len(piles):
        #         return 0
        #     ans = dpf(i + 1, j)
        #     sum = 0
        #     for t in range(1, min(j + 1, len(piles[i]) + 1)):
        #         sum += piles[i][t - 1]
        #         ans = max(ans, dpf(i + 1, j - t) + sum, ans)
        #     dp[i][j] = ans
        #     return ans
        #
        # return dpf(0, k)

        dp = [[-1] * (k + 1) for _ in range(len(piles) + 1)]
        for i in range(len(piles) - 1, -1, -1):
            for j in range(k , -1, - 1):
                if j == 0:
                    dp[i][j] = 0
                else:
                    sum = 0
                    ans = dp[i + 1][j]
                    for t in range(1, min(j + 1, len(piles[i]) + 1, k + 1)):
                        sum += piles[i][t -1 ]
                        ans = max(ans, sum + dp[i + 1][j - t])
                    dp[i][j] = ans
        return dp[0][k]