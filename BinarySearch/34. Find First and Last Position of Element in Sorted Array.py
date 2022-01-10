class Solution:
    def searchRange(self, nums: [int], target: int) -> [int]:
        if len(nums) == 0:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        res = [left]
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        res.append(right)
        return res


test = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(test.searchRange(nums, target))
