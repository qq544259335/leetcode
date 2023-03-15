import heapq
class Solution:
    def maximumProduct(self, nums: [int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(k):
            num = heapq.heappop(nums)
            num += 1
            heapq.heappush(nums,num)
            print(nums)
        res = 1
        for n in nums:
            res *= n
            res = res % (10**9 + 7)
        return res
