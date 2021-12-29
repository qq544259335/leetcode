class Solution:
    # indegree method: node with 0 indegree can be taken, and add it to res,
    # meantime, for all its adjacent node, decrease their indegree by 1
    def findOrder(self, numCourses: int, prerequisites: [[int]]) -> [int]:
        res = []
        adjacent_list = [[] for _ in range(numCourses)]
        indegree_list = [0] * numCourses
        for nextNode, preNode in prerequisites:
            adjacent_list[preNode].append(nextNode)
            indegree_list[nextNode] += 1
        queue = []
        res_set = set()
        for i in range(len(indegree_list)):
            if indegree_list[i] == 0:
                queue.append(i)
                res.append(i)
                res_set.add(i)
        # print(adjacent_list, indegree_list)
        while queue:
            node = queue.pop(0)
            # print(queue, indegree_list, node)

            for adj in adjacent_list[node]:
                # print(adj, node, adjacent_list[node])
                indegree_list[adj] -= 1
                if indegree_list[adj] == 0:
                    queue.append(adj)
                    if adj in res_set:
                        return []
                    res.append(adj)
                    res_set.add(adj)
            # print(queue, indegree_list)
        if len(res) != numCourses:
            return []
        return res


    # dfs
    def findOrderDFS(self, numCourses: int, prerequisites: [[int]]) -> [int]:
        res = []
        adjacent_list = [[] for _ in range(numCourses)]
        for nextNode, preNode in prerequisites:
            adjacent_list[preNode].append(nextNode)
        color_list = [0] * numCourses

        def dfs(node):
            color_list[node] = 1
            for n in adjacent_list[node]:
                if color_list[n] == 1:
                    return []
                elif color_list[n] == 0:
                    dfs(n)
            color_list[node] = 2
            res.insert(0,node)

        for i in range(numCourses):
            if color_list[i] == 0:
                dfs(i)
        if len(res) != numCourses:
            return []
        return res


test = [[1, 0], [2, 0], [3, 1], [3, 2]]
sol = Solution()
print(sol.findOrder(4, test))
test = [[0, 2], [1, 2], [2, 0]]
print(sol.findOrder(3, test))
test = [[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]]
print(sol.findOrder(7, test))
test = [[1, 0], [2, 1], [1, 2]]
print(sol.findOrder(3, test))
