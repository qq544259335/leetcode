class Solution:
    def minimalKSum(self, nums: [int], k: int) -> int:
        sub = 0
        nums = list(set(nums))
        nums.sort()
        for i in range(len(nums)):
            if nums[i] <= k:
                k += 1
                sub += nums[i]
            else:
                break
        return (1 + k) * k // 2 - sub
