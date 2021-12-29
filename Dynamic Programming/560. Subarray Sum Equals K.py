class Solution:
    # https://leetcode.com/problems/subarray-sum-equals-k/solution/
    # n**2 n
    def subarraySum1(self, nums: [int], k: int) -> int:
        l = len(nums)
        sum = [0] * l
        sum[0] = nums[0]
        res = 0
        for i in range(1, l):
            sum[i] = sum[i - 1] + nums[i]
        for i in range(l):
            for j in range(0, i):
                res = res if sum[i] - sum[j] != k else res + 1
            if sum[i] == k:
                res += 1
        return res

    # n**2 1
    def subarraySum2(self, nums: [int], k: int) -> int:
        l = len(nums)
        res = 0
        for i in range(l):
            sum = 0
            for j in range(i, l):
                sum += nums[j]
                if sum == k:
                    res += 1
        return res

    # n n  非常巧妙的方法，对于 sum[i] - k， 如果sum[i] - k 在iteration到达i的时候出现了m次， 就说明有m个新的count -> 需要一个dict统计sum的出现次数
    def subarraySum(self, nums: [int], k: int) -> int:
        sum_dict = {}
        sum = 0
        count = 0
        sum_dict[0] = 1  # 如果没有这个 sum = k就不能被算入count了
        for num in nums:
            sum += num
            new_count = sum_dict.get(sum - k)
            if new_count:
                count += new_count
            if not sum_dict.get(sum):
                sum_dict[sum] = 0
            sum_dict[sum] += 1
        return count


test = Solution()
nums = [1, 2, 3, 6, 0, 7, 5, 1, 9, 4, 3, 3]
k = 6
print(test.subarraySum(nums, k))
