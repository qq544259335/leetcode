class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_remove = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop(-1)
                else:
                    to_remove.append(i)
        remove = set(to_remove + stack)
        res = ""
        for i in range(len(s)):
            if i not in remove:
                res += s[i]
        return res


test = Solution()
input = "lee(t(c)o)de)"
print(test.minRemoveToMakeValid(input))
