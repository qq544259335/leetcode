class Solution:
    def partition(self, s: str) -> [[str]]:
        res = []
        temp = []
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

        def dfs(start, end):
            if start > end:
                save = temp[:]
                res.append(save)
            for i in range(start, end + 1):
                if dp[start][i]:
                    temp.append(s[start:i + 1])
                    dfs(i + 1, end)
                    temp.pop(-1)

        dfs(0, len(s) - 1)
        return res


n = "abcdefd"
sol = Solution()
print(sol.partition(n))
