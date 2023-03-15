from collections import deque

# favorite
class Solution:
    def possibleBipartition(self, n: int, dislikes: [[int]]) -> bool:
        adj_list = [[] for _ in range(n + 1)]
        for i, j in dislikes:
            adj_list[i].append(j)
            adj_list[j].append(i)
        colors = [-1] * (n + 1)
        for i in range(1, n + 1):
            if colors[i] != - 1:
                continue
            else:
                queue = deque()
                queue.append(i)
                colors[i] = 0
                while queue:
                    n = queue.popleft()
                    for node in adj_list[n]:
                        if colors[node] == -1:
                            colors[node] = 1 - colors[n]
                            queue.append(node)
                        elif colors[node] == colors[n]:
                            return False
                        else:
                            continue
        return True

    def possibleBipartitionDFS(self, n: int, dislikes: [[int]]) -> bool:
        adj_list = [[] for _ in range(n + 1)]
        colors = [-1] * (n + 1)
        for i, j in dislikes:
            adj_list[i].append(j)
            adj_list[j].append(i)

        def dfs(n):
            for node in adj_list[n]:
                if colors[node] == colors[n]:
                    return False
                elif colors[node] == -1:
                    colors[node] = 1 - colors[n]
                    if not dfs(node):
                        return False
                else:
                    continue
            return True

        for i in range(1, n + 1):
            if colors[i] != -1:
                continue
            else:
                colors[i] = 0
                if not dfs(i):
                    return False
        return True

    class UnionFind:
        def __init__(self, size):
            self.parent = list(range(size))
            self.rank = [0] * size

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])

            return self.parent[x]

        def union_set(self, x, y):
            xset = self.find(x)
            yset = self.find(y)
            if xset == yset:
                return

            if self.rank[xset] < self.rank[yset]:
                self.parent[xset] = yset
            elif self.rank[xset] > self.rank[yset]:
                self.parent[yset] = xset
            else:
                self.parent[yset] = xset
                self.rank[xset] += 1

    class Solution:
        def possibleBipartitionUnionFound(self, n: int, dislikes: [[int]]) -> bool:
            adj = [[] for _ in range(n + 1)]
            for dislike in dislikes:
                adj[dislike[0]].append(dislike[1])
                adj[dislike[1]].append(dislike[0])

            dsu = Solution.UnionFind(n + 1)
            for node in range(1, n + 1):
                for neighbor in adj[node]:
                    # Check if the node and its neighbor is in the same set.
                    if dsu.find(node) == dsu.find(neighbor): return False
                    # Move all the neighbours into same set as the first neighbour.
                    dsu.union_set(adj[node][0], neighbor)

            return True


dislikes = [[1, 2], [1, 3], [2, 3]]
n = 3
sol = Solution()
print(sol.possibleBipartitionDFS(n, dislikes))
