import heapq
import random

class Solution:
    def kClosestKHeap(self, points: [[int]], k: int) -> [[int]]:  # nlogk logk is the cost of heappushpop
        distances = [(-(x * x + y * y), i) for i, (x, y) in
                     enumerate(points[:k])]  # so that we can relate index with distance
        heapq.heapify(distances)
        for i in range(k, len(points)):
            x, y = points[i]
            dis = -(x * x + y * y)
            heapq.heappushpop(distances, (dis, i))
        res = [points[i] for _, i in distances]
        return res

    def KClosestQuickSort(self, points: [[int]], k: int) -> [[int]]:  # logn
        self.quickSort(points, 0, len(points) - 1, k)
        return points[:k]

    def quickSort(self, points: [int], l: int, r: int, k: int):
        if l < r:
            p = self.partition(points, l, r)
            if p == k:
                return
            if p < k:
                self.quickSort(points, p + 1, r, k)
            if p > k:
                self.quickSort(points, l, p - 1, k)
        return

    def partition(self, points: [int], l: int, r: int) -> int:
        rand = random.randrange(l,r + 1)
        points[rand], points[r] = points[r], points[rand]
        j = l
        for i in range(l, r):
            if (points[i][0] ** 2 + points[i][1] ** 2) <= (points[r][0] ** 2 + points[r][1] ** 2):
                points[i], points[j] = points[j], points[i]
                j += 1
        points[r], points[j] = points[j], points[r]
        return j


sol = Solution()
points = [[2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [1, 1]]
k = 1
print(sol.KClosestQuickSort(points, k))
