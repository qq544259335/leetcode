# https://leetcode-cn.com/problems/stone-game/
class Solution:
    def stoneGame(self, piles: [int]) -> bool:
        dp = [[0] * len(piles) for _ in range(len(piles))]
        for i in range(len(piles)):
            dp[i][i] = piles[i]
        for i in range(len(piles) - 2, -1, -1):
            for j in range(i + 1, len(piles)):
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        print(dp)
        if dp[0][-1] > 0:
            return True
        else:
            return False

sol = Solution()
piles = [5,3,4,5]
print(piles)
print(sol.stoneGame(piles))