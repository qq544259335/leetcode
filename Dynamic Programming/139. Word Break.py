class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            can = False
            for w in wordDict:
                if len(w) <= i and dp[i - len(w)] == True and w == s[i - len(w):i]:
                    can = True
            dp[i] = can
        return dp[-1]
