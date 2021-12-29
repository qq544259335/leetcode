import heapq


class Solution:
    # nlogn n
    def maxSlidingWindowHeap(self, nums: [int], k: int) -> [int]:
        heap = []
        res = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        res.append(-heap[0][0])
        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            while heap[0][1] < (i - k + 1):
                heapq.heappop(heap)
            res.append(-heap[0][0])
        return res


    # 很秀 https://leetcode-cn.com/problems/sliding-window-maximum/solution/hua-dong-chuang-kou-zui-da-zhi-by-leetco-ki6m/
    # n k

    def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
        queue = [0]
        for i in range(1, k):
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop(-1)
            queue.append(i)
        res = [nums[queue[0]]]
        for i in range(k, len(nums)):
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop(-1)
            queue.append(i)
            while queue[0] <= i - k:
                queue.pop(0)
            res.append(nums[queue[0]])
        return res