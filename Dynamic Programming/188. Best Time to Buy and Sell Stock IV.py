class Solution:
    def maxProfit(self, k: int, prices: [int]) -> int:
        n = len(prices)
        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(len(prices) + 1)]
        for i in range(k + 1):
            dp[0][i][0] = 0
            dp[0][i][1] = float('-inf')
        for i in range(n + 1):
            dp[i][0][0] = 0
            dp[i][0][1] = float('-inf')
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i - 1])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][k - 1][0] - prices[i - 1])
                if dp[i][j][0] == dp[i - 1][j][1] + prices[i - 1]:
                    print("sell ", i, j)
                if dp[i][j][1] == dp[i - 1][k - 1][0] - prices[i - 1]:
                    print("buy ", i, j)
        for i in range(n + 1):
            print(dp[i])
        return dp[n][k][0]


test = Solution()
k = 2
prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(test.maxProfit(k, prices))
