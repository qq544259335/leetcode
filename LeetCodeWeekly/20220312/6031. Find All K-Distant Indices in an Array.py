class Solution:
    def findKDistantIndices(self, nums: [int], key: int, k: int) -> [int]:
        indexs = []
        for i in range(len(nums)):
            if nums[i] == key:
                indexs.append(i)
        res = set()
        for i in range(len(indexs)):
            for temp in range(max(0,indexs[i] - k), min(len(nums), indexs[i] + k + 1)):
                res.add(temp)
        return list(res)