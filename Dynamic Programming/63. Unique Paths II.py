class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: [[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        cur = [0] * n
        cur[0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    cur[j] = 0
                else:
                    left = cur[j - 1] if j >= 1 else 0
                    cur[j] = left + cur[j]
        return cur[-1]

    def uniquePathsWithObstacles20210626(self, obstacleGrid: [[int]]) -> int:
        dp = [0] * len(obstacleGrid[0])
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                print(i, j, dp)
                if i != 0:
                    dp[j] = dp[j] + dp[j - 1] if j - 1 >= 0 else dp[j]
                else:
                    dp[j] = dp[j - 1] if j - 1 >= 0 else 1
                dp[j] = dp[j] if obstacleGrid[i][j] == 0 else 0
                print(i, j, dp)
        return dp[-1]


sol = Solution()
array = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
array2 = [[1, 0]]
print(sol.uniquePathsWithObstacles20210626(array2))
