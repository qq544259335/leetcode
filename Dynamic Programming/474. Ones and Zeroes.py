class Solution:
    def findMaxForm(self, strs: [str], m: int, n: int) -> int:
        counts = []
        for s in strs:
            count_0 = 0
            count_1 = 0
            for c in s:
                if c == '0':
                    count_0 += 1
                else:
                    count_1 += 1
            counts.append((count_0, count_1))
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for x, y in counts:
            for i in range(m, x - 1, -1):
                for j in range(n, y - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - x][j - y])
        return dp[-1][-1]


test = Solution()
strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
print(test.findMaxForm(strs, m, n))
