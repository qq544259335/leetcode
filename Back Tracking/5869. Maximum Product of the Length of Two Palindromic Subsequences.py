class Solution:
    def maxProduct(self, s: str) -> int:
        subStrings = []
        temp = ""
        def dfs(cur):
            if cur == len(s):
                return
            for i in range(cur,len(s)):


sol = Solution()
print(sol.maxProduct("leetcodecom"))