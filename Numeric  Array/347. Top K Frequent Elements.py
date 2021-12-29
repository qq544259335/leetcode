class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        if len(nums) == 0:
            return []
        d = {}
        for n in nums:
            if n not in d.keys():
                d[n] = 0
            d[n] += 1
        bucket = [[] for _ in range(len(nums) + 1)]
        for key in d.keys():
            bucket[d[key]].append(key)
        res = []
        for elements in reversed(bucket):
            for element in elements:
                res.append(element)
                k -= 1
                if k == 0:
                    return res
