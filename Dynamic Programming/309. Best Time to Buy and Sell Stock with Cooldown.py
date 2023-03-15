class Solution:
    def maxProfit(self, prices: [int]) -> int:
        dp0 = 0
        dp1 = float('-inf')
        dp0_1 = 0
        for i in range(1, len(prices) + 1):
            dp0, dp1,dp0_1 = max(dp0, dp1 + prices[i - 1]), max(dp1, dp0_1 - prices[i - 1]), dp0
        return dp0