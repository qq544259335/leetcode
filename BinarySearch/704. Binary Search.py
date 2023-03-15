class Solution:
    def search(self, nums: [int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = i + (j - i) // 2
            print(i, mid, j)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return -1


