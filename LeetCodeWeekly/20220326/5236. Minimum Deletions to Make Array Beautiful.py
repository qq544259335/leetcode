class Solution:
    def minDeletion(self, nums: [int]) -> int:
        i = 0
        count = 0
        while i + 1 < len(nums):
            if nums[i] == nums[i + 1]:
                count += 1
                i += 1
            else:
                i += 2
        if (len(nums) - count) % 2 == 1:
            count += 1
        return count
