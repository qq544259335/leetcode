class Solution:
    def maximumEvenSplit(self, finalSum: int) -> [int]:
        if finalSum % 2 != 0:
            return []
        count_2 = finalSum // 2
        cur = 0
        res = []
        while count_2 > 0:
            cur += 1
            if count_2 - cur == 0:
                res.append(2 * cur)
                return res
            if count_2 - cur > cur:
                res.append(2 * cur)
                count_2 -= cur
