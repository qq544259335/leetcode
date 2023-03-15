class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start_b = bin(start)[2:]
        goal_b = bin(goal)[2:]
        l = max(len(start_b), len(goal_b))
        while l > len(start_b):
            start_b = "0" + start_b
        while l > len(goal_b):
            goal_b = "0" + goal_b
        print(start_b, goal_b)
        res = 0
        for i in range(l):
            if start_b[i] != goal_b[i]:
                res += 1
        return res
