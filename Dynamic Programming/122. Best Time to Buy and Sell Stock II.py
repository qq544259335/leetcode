class Solution:
    def maxProfit(self, prices: [int]) -> int:
        dp0 = 0
        dp1 = float('-inf')
        for i in range(1, len(prices) + 1):
            dp0, dp1 = max(dp0, dp1 + prices[i - 1]), max(dp1, dp0 - prices[i - 1])
        return dp0

    def maxProfitGreedy(self, prices: [int]) -> int:
        max_profit = 0
        i = 1
        while i < len(prices):
            while i < len(prices) and prices[i] >= prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
                i += 1
            i += 1
        return max_profit