class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[-1] if dp[-1] != amount + 1 else -1

    def coinChangeRecursion(self, coins: [int], amount: int) -> int:
        def dp(n: int) -> int:
            if n < 0:
                return -1
            if n == 0:
                res[0] = 0
                return res[0]
            if res[n] != float('-inf'):
                return res[n]
            temp_res = 10**5
            for c in coins:
                sub = dp(n - c)
                if sub == -1: continue
                temp_res = min(temp_res, sub + 1)
            res[n] = -1 if temp_res == 10**5 else temp_res
            return res[n]

        res = [float('-inf')] * (amount + 1)
        return dp(amount)


coins = [2]
amount = 3
test = Solution()
print(test.coinChange(coins, amount))
