class Solution:
    def numberOfWays(self, corridor: str) -> int:
        res = 1
        count = 0
        s_pos = []
        for i in range(len(corridor)):
            if corridor[i] == "S":
                count += 1
                s_pos.append(i)
        if count % 2 == 1 or count == 0:
            return 0
        p = 2
        while p < len(s_pos):
            res *= s_pos[p] - s_pos[p - 1]
            p += 1
            if p >= len(s_pos):
                return res
            p += 1
        return res
