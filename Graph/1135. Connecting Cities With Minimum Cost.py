class Solution:
    def minimumCost(self, n: int, connections: [[int]]) -> int:
        totalCost = 0
        edgeCount = 0
        self.father = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)
        connections.sort(key=lambda connections: connections[2])
        for u, v, cost in connections:
            rootU = self.findFather(u)
            rootV = self.findFather(v)
            if rootU != rootV:
                if self.size[rootU] > self.size[rootV]:
                    rootU, rootV = rootV, rootU
                self.father[rootU] = rootV
                self.size[rootV] += self.size[rootU]
                totalCost += cost
                edgeCount += 1
        if edgeCount == n - 1:
            return totalCost
        return - 1

    def findFather(self, n: int):
        if self.father[n] == n:
            return n
        self.father[n] = self.findFather(self.father[n])
        return self.father[n]
