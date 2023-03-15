class Solution:
    def maxProfit(self, prices: [int], fee: int) -> int:
        dp0 = 0
        dp1 = float('-inf')
        for i in range(1, len(prices) + 1):
            dp0, dp1 = max(dp0, dp1 + prices[i - 1]), max(dp1, dp0 - prices[i - 1]- fee)
        return dp0