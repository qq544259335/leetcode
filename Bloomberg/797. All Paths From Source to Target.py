class Solution:
    def allPathsSourceTarget(self, graph: [[int]]) -> [[int]]:
        res = []
        stack = []
        node_max = len(graph) - 1
        def dfs(node):
            if node == node_max:
                res.append(stack[:])
                return
            for next in graph[node]:
                stack.append(next)
                dfs(next)
                stack.pop(-1)

        stack.append(0)
        dfs(0)
        return res