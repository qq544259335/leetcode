class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.matchFunc(s, p, "")

    def matchFunc(self, s: str, p: str, prev: str) -> bool:
        print("s:{}, p:{}".format(s, p))
        if s == "":
            if p == "":
                return True
            else:
                while len(p) >= 2:
                    p1 = p[0]
                    p2 = p[1]
                    if ("z" >= p1 >= "a" or p1 == ".") and p2 == "*":
                        p = p[2:]
                    else:
                        return False
                return True if len(p) == 0 else False
        elif p == "":
            return False
        pattern = p[0]
        if len(p) >= 2 and p[1] == "*":
            prev = p[0]
            compare = prev
            if prev == ".":
                compare = s[0]
            if s[0] != compare:
                return self.matchFunc(s, p[2:], prev)
            else:
                if not self.matchFunc(s[1:], p, prev):
                    return self.matchFunc(s, p[2:], prev)
                else:
                    return True
        else:
            if "z" >= pattern >= "a":
                if s[0] == pattern:
                    return self.matchFunc(s[1:], p[1:], s[0])
                else:
                    return False
            if pattern == ".":
                return self.matchFunc(s[1:], p[1:], s[0])
            else:
                return False

    def isMatchFaster(self, s: str, p: str) -> bool:  # turned the backtrack recursion to iteration
        def match(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == ".":
                return True
            else:
                return s[i - 1] == p[j - 1]

        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2]
                    dp[i][j] |= dp[i - 1][j] if match(i, j - 1) else dp[i][j]
                else:
                    dp[i][j] = dp[i - 1][j - 1] if match(i, j) else dp[i][j]
        return dp[m][n]


testS3 = "aabcbcbcaccbcaabc"
testP3 = ".*a*aa*.*b*.c*.*a*"
testS = "mississippi"
testP = "mis*is*p*."
testS2 = "aaa"
testP2 = "a*a"
sol = Solution()
print(sol.isMatchFaster(testS3, testP3))
