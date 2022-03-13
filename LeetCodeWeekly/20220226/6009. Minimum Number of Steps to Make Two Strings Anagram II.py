class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        for c in t:
            count[ord(c) - ord('a')] -= 1
        res = 0
        for n in count:
            res += abs(n)
        return res


test = Solution()
print(test.minSteps("leetcode", "coats"))