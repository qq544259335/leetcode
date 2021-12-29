class Solution:
    # double pointerTime NlogN Space N
    def twoSum(self, nums: [int], target: int) -> [int]:
        index_num = []
        for i in range(len(nums)):
            index_num.append((i, nums[i]))
        index_num = sorted(index_num, key=lambda x: x[1])
        i = 0
        j = len(nums) - 1
        while i < j:
            if index_num[i][1] + index_num[j][1] == target:
                return [index_num[i][0], index_num[j][0]]
            elif index_num[i][1] + index_num[j][1] > target:
                j -= 1
            else:
                i += 1

    def twoSumHash(self, nums: [int], target: int) -> [int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in d.keys() and i != d[target - nums[i]]:
                return [i, d[target - nums[i]]]
        