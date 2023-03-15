class Solution:
    def maxProfit(self, k: int, prices: [int]) -> int:
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(len(prices) + 1)]
        for i in range(k + 1):
            dp[0][i][0] = 0
            dp[0][i][1] = float('-inf')
        for i in range(len(prices) + 1):
            dp[i][0][0] = 0
            dp[i][0][1] = float('-inf')
        for i in range(1, len(prices) + 1):
            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i - 1])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i - 1])
        return dp[-1][-1][0]

sol = Solution()
print(sol.maxProfit(5,[1,23,12,4,124,123]))