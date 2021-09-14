class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:  # O(n)  user sliding window
        # it is obvious that there is a hidden feature: when we find a substring with length l, we do not need to
        # find any shorter substring
        res, right = 0, - 1
        charSet = set()
        for i in range(len(s)):
            if i != 0:
                charSet.remove(s[i - 1])
            while right + 1 < len(s) and s[right + 1] not in charSet:
                charSet.add(s[right + 1])
                right += 1
            res = max(res, right - i + 1)
        return res

    def lengthOfLongestSubstringSlow(self, s: str) -> int:  # O(n**2)
        res = 0
        for i in range(len(s)):
            charSet = set()
            length = 0
            for j in range(i, len(s)):
                print(charSet)
                if s[j] not in charSet:
                    charSet.add(s[j])
                    length += 1
                else:
                    print(length)
                    res = length if length > res else res
                    break
            res = length if length > res else res
        return res


string = "abcdeeeaqwerz"
sol = Solution()
print(sol.lengthOfLongestSubstring(string))
