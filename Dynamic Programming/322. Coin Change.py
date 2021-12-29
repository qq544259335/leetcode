class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            print(dp)
            min_num = float('inf')
            for c in coins:
                if i - c >= 0:
                    if dp[i - c] >= 0:
                        min_num = min(min_num, dp[i - c] + 1)
            dp[i] = min_num if min_num != float('inf') else dp[i]
            print(dp)
        return dp[-1]

coins = [2]
amount = 3
test = Solution()
print(test.coinChange(coins,amount))