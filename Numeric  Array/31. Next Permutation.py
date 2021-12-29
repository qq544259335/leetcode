class Solution:
    def nextPermutation(self, nums: [int]) -> None:
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                j = i
                while j < len(nums) and nums[i - 1] < nums[j]:
                    j += 1
                j -= 1
                nums[i - 1], nums[j] = nums[j], nums[i - 1]
                reverse(i, len(nums) - 1)
                return nums
        reverse(0, len(nums) - 1)
        return nums



test = Solution()
print(test.nextPermutation([3, 2, 1]))
