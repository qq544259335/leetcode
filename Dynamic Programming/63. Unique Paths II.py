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