import heapq


class Solution:
    def halveArray(self, nums: [int]) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        sum_nums = -sum(nums)
        cur_sum = sum_nums
        count = 0
        while cur_sum > 0.5 * sum_nums:
            sub = heapq.heappop(nums)
            sub = sub / 2
            heapq.heappush(nums, sub)
            cur_sum += sub
            count += 1
        return count