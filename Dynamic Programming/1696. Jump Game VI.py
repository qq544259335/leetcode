import heapq
from collections import deque

class Solution:
    def maxResult(self, nums: [int], k: int) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            q = float('-inf')
            for j in range(1, k + 1):
                if j <= i:
                    q = max(q, dp[i - j] + nums[i])
            dp[i] = q
        return dp[-1]



    def maxResultHeap(self, nums: [int], k: int) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        heap = []
        heapq.heappush(heap, (-dp[0], 0))
        for i in range(1, len(nums)):
            while heap[0][1] < i - k:
                heapq.heappop(heap)
            cur = heap[0][0] - nums[i]
            dp[i] = -cur
            heapq.heappush(heap, (cur, i))
        return dp[-1]

    def maxResultQueue(self, nums: [int], k: int) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        q = deque()
        q.append(0)
        for i in range(1, len(nums)):
            while q[0] < i - k:
                q.popleft()
            cur = dp[q[0]] + nums[i]
            dp[i] = cur
            while q and dp[q[-1]] < cur:
                q.pop()
            q.append(i)
        return dp[-1]