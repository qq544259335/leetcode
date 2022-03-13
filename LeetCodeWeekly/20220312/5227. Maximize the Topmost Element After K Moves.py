class Solution:
    def maximumTop(self, nums: [int], k: int) -> int:
        if k == 0:
            return nums[0]
        if len(nums) == 1 and k % 2 == 1:
            return -1
        if k == 1:
            return nums[1]
        if len(nums) < k:
            return max(nums)
        elif len(nums) == k:
            return max(nums[:-1])
        else:
            max_possible = max(max(nums[:k - 1]), nums[k])
            return max_possible