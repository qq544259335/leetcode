class Solution:
    def longestPalindrome(self, s: str) -> str: # 标准解法，但是超时
        length = len(s)
        dp = []
        maxCount = ""
        for i in range(length):
            dp.append([0] * length)
        for count in range(length):
            for i in range(length):
                j = i + count
                if j >= length:
                    break
                if j == i:
                    dp[i][j] = True
                elif j == i + 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]
                if dp[i][j] and count + 1 > len(maxCount):
                    maxCount = s[i:j + 1]
        return maxCount

    def longestPalindrome2(self, s: str) -> str:
        def getLongest(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        start, end = 0, 0
        for i in range(len(s)):
            left, right = getLongest(s, i, i)
            if i + 1 < len(s):
                left2, right2 = getLongest(s, i, i + 1)
                if right2 - left2 > right - left:
                    left = left2
                    right = right2
            if right - left > end -start:
                start = left
                end = right
        return s[start: end + 1]


solve = Solution()
print(solve.longestPalindrome2("ababaa"))
