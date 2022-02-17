import heapq


class Solution:
    def minimumDifference(self, nums: [int]) -> int:
        n = len(nums) // 3
        small_heap = []
        small_sum = 0
        for i in range(n):
            small_heap.append(-nums[i])
            small_sum += nums[i]
        heapq.heapify(small_heap)
        big_heap = nums[2*n:3 * n]
        big_sum = 0
        for i in range(n):
            big_sum += big_heap[i]
        heapq.heapify(big_heap)
        bigs = [0] * (n + 1)
        smalls = [0] * (n + 1)
        smalls[0] = small_sum
        bigs[-1] = big_sum
        print(nums, small_heap, smalls, big_heap, bigs)
        for i in range(0, n):
            p = i + n
            heapq.heappush(small_heap, -nums[p])
            big_in_small = -heapq.heappop(small_heap)
            smalls[i + 1] = smalls[i] + nums[p] - big_in_small
        for j in range(2*n - 1, n - 1, - 1):
            heapq.heappush(big_heap, nums[j])
            small_in_big = heapq.heappop(big_heap)
            print(small_in_big, bigs[j -n + 1], nums[j])
            bigs[j - n] = bigs[j - n + 1] + nums[j] - small_in_big
        res = smalls[0] - bigs[0]
        for i in range(1, n + 1):
            res = min(res, smalls[i] - bigs[i])
        print(smalls,bigs)
        return res


test = Solution()
nums = [7,9,5,8,1,3]
print(test.minimumDifference(nums))
