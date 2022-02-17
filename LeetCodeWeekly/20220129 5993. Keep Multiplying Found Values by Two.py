class Solution:
    def findFinalValue(self, nums: [int], original: int) -> int:
        if len(nums) == 0:
            return original
        nums.sort()
        last = 0
        while original <= nums[-1]:
            for i in range(last, len(nums)):
                if nums[i] == original:
                    original *= 2
                    last = i
                    break
                elif nums[i] > original:
                    return original
        return original
