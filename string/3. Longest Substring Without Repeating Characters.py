class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans
    def lengthOfLongestSubstringNotFast(self, s: str) -> int:  # O(n)  user sliding window
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

    def lengthOfLongestSubstring2(self, s: str) -> int:
        res = 0
        char_dict = {}
        left = 0
        right = 0

        def not_dup():
            for k in char_dict:
                if char_dict[k] > 1:
                    return False
            return True

        while right < len(s):
            if s[right] not in char_dict.keys():
                char_dict[s[right]] = 0
            char_dict[s[right]] += 1
            right += 1
            while not not_dup() and left < len(s):
                char_dict[s[left]] -= 1
                left += 1
            length = right - 1 - left + 1
            res = max(res, length)
        return res


string = "abcdeeeaqwerz"
sol = Solution()
print(sol.lengthOfLongestSubstring(string))
