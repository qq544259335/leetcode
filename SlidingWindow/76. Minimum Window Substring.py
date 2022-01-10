class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        if len(t) == 0:
            return ""
        left = 0
        right = 0
        res = ""
        length = float('inf')
        check_set = set(t)
        char_count = {}
        for c in t:
            if c in check_set:
                if c not in char_count:
                    char_count[c] = 0
                char_count[c] -= 1

        def contains_all():
            for k, v in char_count.items():
                print(char_count)
                if v < 0:
                    return False
            return True

        while right < len(s):
            while not contains_all():
                if right >= len(s):
                    return res
                cur = s[right]
                right += 1
                if cur in check_set:
                    char_count[cur] += 1
            while contains_all():
                cur = s[left]
                left += 1
                if cur in check_set:
                    char_count[cur] -= 1
            print(left - 1, right, s[left - 1:right])
            if right - 1 - left + 1 + 1 < length:
                res = s[left - 1:right]
                length = right - 1 - left + 1 + 1
        return res


s = "ab"
t = "a"
test = Solution()
print(test.minWindow(s, t))
