class Solution:
    def countHillValley(self, nums: [int]) -> int:
        res = 0
        for i in range(len(nums) - 1):
            if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                nums.pop(i)
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                res += 1
            if nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                res += 1
        return res