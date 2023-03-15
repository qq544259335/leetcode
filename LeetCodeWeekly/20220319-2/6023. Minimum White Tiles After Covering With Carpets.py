class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        dp = [[0] * (numCarpets + 1) for _ in range(len(floor) + 1)]
        for i in range(1, len(floor) + 1):
            for j in range(numCarpets + 1):
                jump = dp[i - 1][j] + int(floor[i - 1])
                select =  dp[max(i - carpetLen,0)][j - 1] if j > 0 else 1000
                dp[i][j] = min(jump,select)
        return dp[-1][-1]