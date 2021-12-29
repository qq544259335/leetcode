class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        if intervals:
            res = []
            temp = []
            last = -1
            intervals = sorted(intervals, key=lambda x: x[0])
            while intervals:
                inter = intervals.pop(0)
                if inter[0] > last:
                    if temp:
                        res.append(temp)
                    temp = inter[:]
                else:
                    if inter[1] > temp[1]:
                        temp[1] = inter[1]
                last = temp[1]
            if temp:
                res.append(temp)
            return res
        else:
            return []