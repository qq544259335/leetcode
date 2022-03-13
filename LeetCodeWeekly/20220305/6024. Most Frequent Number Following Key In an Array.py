class Solution:
    def mostFrequent(self, nums: [int], key: int) -> int:
        count_dict = {}
        for i in range(len(nums) - 1):
            if nums[i] == key:
                if nums[i + 1] not in count_dict:
                    count_dict[nums[i + 1]] = 0
                count_dict[nums[i + 1]] += 1
        max_count = -1
        res = - 1
        for k, v in count_dict.items():
            if v > max_count:
                res = k
                max_count = v
        return res
