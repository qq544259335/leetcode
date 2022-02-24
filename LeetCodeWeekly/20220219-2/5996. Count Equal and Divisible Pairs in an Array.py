class Solution:
    def countPairs(self, nums: [int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and i * j % k == 0:
                    res += 1
        return res


test = Solution()
print(test.countPairs([3, 1, 2, 2, 2, 1, 3], 2))
