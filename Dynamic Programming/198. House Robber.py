class Solution:
    def rob(self, nums: [int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [0] * (len(nums) + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(1, len(nums)):
            dp[i + 1] = max(dp[i], dp[i - 1] + nums[i])
        return dp[-1]

    def rob2(self, nums: [int]) -> int:
        if len(nums) == 0:
            return 0
        pre = 0
        cur = 0
        for i in range(len(nums)):
            cur, pre = max(cur, pre + nums[i]), cur
        return cur

sol = Solution()
print(sol.rob([1,2,3,4,5,6]))