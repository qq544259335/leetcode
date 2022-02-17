class Solution:
    def findLonely(self, nums: [int]) -> [int]:
        nums.sort()
        res = []
        if len(nums) <= 1:
            return nums
        for i in range(len(nums)):
            left = i - 1
            right = i + 1
            if i == 0:
                if nums[1] > nums[0] + 1:
                    res.append(nums[0])
            elif i == len(nums) - 1:
                if nums[len(nums) - 1] > nums[len(nums) - 1 - 1] + 1:
                    res.append(nums[len(nums) - 1])
            else:
                if nums[i] > nums[left] + 1 and nums[right] > nums[i] + 1:
                    res.append(nums[i])
        return res
