class Solution:
    def getAncestors(self, n: int, edges: [[int]]) -> [[int]]:
        adjacent = [[] for _ in range(n)]
        for s, e in edges:
            adjacent[s].append(e)
        res = [set() for _ in range(n)]
        starter = [True] * n
        for s, e in edges:
            starter[e] = False
        nodes = []
        for i in range(n):
            if starter[i]:
                nodes.append(i)
        while nodes:
            length = len(nodes)
            for i in range(length):
                node = nodes.pop(0)
                for adj in adjacent[node]:
                    res[adj].add(node)
                    for n in res[node]:
                        res[adj].add(n)
                    if adj not in nodes:
                        nodes.append(adj)
        for i in range(len(res)):
            res[i] = list(res[i])
            res[i].sort()
        return res
