class Solution:
    def twoSum(self, numbers: [int], target: int) -> [int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            num = numbers[l] + numbers[r]
            if num == target:
                return [l + 1, r + 1]
            elif num < target:
                l = l + 1
            else:
                r = r - 1
        return [-1, -1]
