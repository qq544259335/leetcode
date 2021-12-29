class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        res = ""
        i = 0
        while True:
            if i > len(strs[0]) - 1:
                return res
            res += strs[0][i]
            for s in strs[1:len(strs)]:
                if i > len(s) - 1 or s[i] != res[-1]:
                    return res[:-1]
            i += 1


test = Solution()
input = ["", "flower"]
print(test.longestCommonPrefix(input))