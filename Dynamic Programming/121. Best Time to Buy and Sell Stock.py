class Solution:
    def maxProfit(self, prices: [int]) -> int:
        max_profit = 0
        buy = 0
        sell = 1
        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            if profit >= 0:
                max_profit = max(max_profit, profit)
            else:
                buy = sell
            sell += 1
        return max_profit
