class Solution:
    def minimumTime(self, s: str) -> int:
        dp = [0] * len(s)
        for i in range(len(s)):
            c = -1 if s[i] == "0" else 1
            dp[i] = min(dp[i - 1] + c, c) if i != 0 else dp[i]
        return min(min(dp) + len(s), len(s))


test = Solution()
s = "111100000111"
print(test.minimumTime(s))
