class Solution:
    def checkValidString(self, s: str) -> bool:  # looks like backtrack
        maxCount = 0
        minCount = 0
        for c in s:
            if c == "(":
                maxCount += 1
                minCount += 1
            elif c == ")":
                minCount = max(minCount - 1, 0)
                maxCount -= 1
                if maxCount < 0:
                    return False
            else:
                minCount = max(minCount - 1, 0)
                maxCount += 1
        return minCount == 0

    def checkValidStringStack(self, s: str) -> bool:  # looks like backtrack
        leftStack = []
        starStack = []
        for i in range(len(s)):
            if s[i] == "(":
                leftStack.append(i)
            elif s[i] == "*":
                starStack.append(i)
            else:
                if len(leftStack) != 0:
                    leftStack.pop(-1)
                elif len(starStack) != 0:
                    starStack.pop(-1)
                else:
                    return False
        while len(leftStack) != 0 and len(starStack) != 0:
            print(leftStack, starStack)
            left = leftStack.pop(0)
            right = starStack.pop(0)
            while left >= right:
                if len(starStack) == 0:
                    return False
                right = starStack.pop(0)
        if len(leftStack) != 0:
            return False
        return True

test = ")"
sol = Solution()
print(sol.checkValidString(test))
