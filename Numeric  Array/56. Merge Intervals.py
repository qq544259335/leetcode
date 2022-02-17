class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for i in range(len(intervals)):
            if not res or intervals[i][0] > res[-1][-1]:
                res.append(intervals[i])
            else:
                res[-1][-1] = max(intervals[i][1], res[-1][-1])
        return res
