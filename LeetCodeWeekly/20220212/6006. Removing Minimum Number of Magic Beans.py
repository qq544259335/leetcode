class Solution:
    def minimumRemoval(self, beans: [int]) -> int:
        res = float('inf')
        beans.sort()
        sum_all = sum(beans)
        for i in range(len(beans)):
            res = min(res, sum_all - (len(beans) - i) * beans[i])
        return res