class Solution:
    def numberOfArrays(self, differences: [int], lower: int, upper: int) -> int:
        cur = 0
        min_num = 0
        max_num = 0
        for num in differences:
            cur += num
            min_num = min(min_num, cur)
            max_num = max(max_num, cur)
        diff = lower - min_num
        max_num += diff
        return upper - max_num + 1 if upper - max_num + 1 >= 0 else 0
