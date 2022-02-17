class Solution:
    def countElements(self, nums: [int]) -> int:
        max_n = float('-inf')
        min_n = float('inf')
        for n in nums:
            max_n = max(max_n, n)
            min_n = min(min_n, n)
        res = 0
        for n in nums:
            if n != max_n and n != min_n:
                res += 1
        return res
