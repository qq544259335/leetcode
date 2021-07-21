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

    def longestPalindrome20210617(self, s: str) -> str:
        dp = [[-1] * len(s) for _ in range(len(s))]
        start = 0
        end = 0
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(len(s) - 2, -1, -1):
            for j in range(i + 1, len(s)):
                dp[i][j] = False
                if s[i] == s[j] and (dp[i + 1][j - 1] == True or dp[i + 1][j - 1] == -1):
                    dp[i][j] = True
                    if abs(start - end) < abs(i - j):
                        start = i
                        end = j
        return s[start: end + 1]

    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome20210617central(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]

solve = Solution()
print(solve.longestPalindrome20210617("aa"))
