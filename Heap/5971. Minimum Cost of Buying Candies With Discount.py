import heapq


class Solution:
    def minimumCost(self, cost: [int]) -> int:
        for i in range(len(cost)):
            cost[i] = -cost[i]
        heapq.heapify(cost)
        print(cost)
        res = 0
        while cost:
            for i in range(2):
                if cost:
                    res += heapq.heappop(cost)
                else:
                    return -res
            if cost:
                heapq.heappop(cost)
            else:
                return -res
        return -res


sol = Solution()
cost = [6, 5, 7, 9, 2, 2]
print(sol.minimumCost(cost))
