class Solution:
    def minCut(self, s: str) -> [[str]]:
        res = [2000] * len(s)
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            for l in (0, 1):
                if i + l >= len(s):
                    continue
                if s[i] == s[i + l]:
                    dp[i][i + l] = True
        for l in range(2, len(s)):
            for i in range(0, len(s) - l):
                j = i + l
                dp[i][j] = dp[i + 1][j - 1] if s[i] == s[j] else False
        for i in range(len(s)):
            if dp[0][i]:
                res[i] = 0
            else:
                for j in range(i):
                    if dp[j + 1][i]:
                        res[i] = min(res[i], res[j] + 1)
        return res[-1]

s = "ababababababababababababcbabababababababababababaa"
sol = Solution()
print(sol.minCut(s))