class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getPalindrome(i: int, j: int) -> str:
            while j >= 0 and i < len(s) and s[i] == s[j]:
                i += 1
                j -= 1
            return s[j + 1: i]

        longest = ""
        for i in range(len(s)):
            temp1 = getPalindrome(i, i)
            temp2 = getPalindrome(i + 1, i)
            temp = temp1 if len(temp1) > len(temp2) else temp2
            longest = temp if len(temp) > len(longest) else longest
        return longest

sol = Solution()
print(sol.longestPalindrome("babab"))