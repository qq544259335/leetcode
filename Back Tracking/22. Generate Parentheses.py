class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        res = []
        temp = []
        right, left = n, n
        def dfs(right, left, count):
            if right == 0 and left == 0:
                res.append("".join(temp))
                return
            for char in ["(", ")"]:
                if char == "(":
                    if right == 0:
                        continue
                    temp.append("(")
                    dfs(right - 1, left, count + 1)
                    temp.pop(-1)
                else:
                    if left == 0 or count <= 0:
                        continue
                    temp.append(")")
                    dfs(right, left - 1, count - 1)
                    temp.pop(-1)

        dfs(right,left, 0)
        return res

test = 1
sol = Solution()
print(sol.generateParenthesis(test))