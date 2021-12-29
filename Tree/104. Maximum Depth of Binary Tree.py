# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, depth):
            if root is None:
                return depth
            d1 = dfs(root.left, depth + 1)
            d2 = dfs(root.right, depth + 1)
            return max(d1, d2)

        return dfs(root, 0)

    def maxDepth2(self, root: TreeNode) -> int:
        if root is None:
            return 0
        height1 = self.maxDepth2(root.left)
        height2 = self.maxDepth2(root.right)
        return max(height1,height2) + 1

    def maxDepthDFS(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = [root]
        res = 0
        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res += 1
        return res