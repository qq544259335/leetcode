class Solution:
    # o(n**2) o(1)
    def countSubstrings(self, s: str) -> int:
        def midExpand(i, j, s):
            sum_res = 0
            while j < len(s):
                expand = 0
                while i - expand >= 0 and j + expand < len(s):
                    if s[i - expand] == s[j + expand]:
                        sum_res += 1
                    else:
                        break
                    expand += 1
                i += 1
                j += 1
            return sum_res
        return midExpand(0, 0, s) + midExpand(0, 1, s)

    # dp o(n**2) o(n**2)
    def countSubstringsDP(self, s: str) -> int:
        dp = [[False]*len(s) for _ in range(len(s))]
        res = 0
        for step in range(len(s)):
            for i in range(len(s) - step):
                if i + 1 > i + step - 1:
                    dp[i][i + step] = s[i] == s[i+ step]
                else:
                    dp[i][i + step] = (s[i] == s[i + step]) and dp[i + 1][i + step -1]
                if dp[i][i+step]:
                    res +=1
        return res

test = Solution()
s = "asdeeea"
print(test.countSubstringsDP(s))