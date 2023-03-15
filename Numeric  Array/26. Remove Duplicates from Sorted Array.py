class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        iter = 0
        update = 0
        while iter < len(nums):
            if nums[iter] == nums[update]:
                iter += 1
            else:
                update += 1
                nums[update] = nums[iter]
        return update + 1
