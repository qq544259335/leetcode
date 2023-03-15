class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        inter = 0
        update = 0
        while inter < len(nums):
            if nums[inter] != val:
                nums[update] = nums[inter]
                update += 1
            inter += 1
        return update