class Solution:
    def change(self, amount: int, coins: [int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for n in range(c, amount + 1):
                dp[n] += dp[n - c]
        return max(0,dp[-1])


sol = Solution()
print(sol.change(5, [1, 2, 5]))
print(sol.change(0, [3]))
print(sol.change(2, [2]))
print(sol.change(3, [2]))
