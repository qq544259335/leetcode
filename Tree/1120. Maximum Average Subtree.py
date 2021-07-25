class TreeNode:
    def __init__(self, x, children: []):
        self.val = x
        self.children = children


class Solution:
    def maxAverage(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.res = [0, None]
        self.dfs(root)
        return self.res[1]

    def dfs(self, root: TreeNode) -> (int, int):
        if root:
            sum, num = root.val, 1
            for node in root.children:
                tempSum, tempNum = self.dfs(node)
                sum += tempSum
                num += tempNum
            average = sum / num
            if num > 1:
                self.res = [average, root] if self.res[0] < average else self.res
            return sum, num


n8 = TreeNode(8, [])
n7 = TreeNode(15, [])
n6 = TreeNode(3, [])
n5 = TreeNode(2, [])
n4 = TreeNode(11, [])
n3 = TreeNode(18, [n7, n8])
n2 = TreeNode(12, [n4, n5, n6])
n1 = TreeNode(20, [n2, n3])

solution = Solution()
print(solution.maxAverage(n1).val)
for node in solution.maxAverage(n1).children:
    print(node.val)
print("node val with highest average", solution.maxAverage(n1).val)