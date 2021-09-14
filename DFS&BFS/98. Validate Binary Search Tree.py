# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.dfs(root, -2 ** 31 - 1, 2 ** 31)

    def dfs(self, root: TreeNode, start: int, end: int) -> bool:
        if not root:
            return True
        if end > root.val > start:
            return self.dfs(root.left, start, min(end, root.val)) and self.dfs(root.right, max(start, root.val), end)
        return False


node5 = TreeNode(3)
node4 = TreeNode(7)
node3 = TreeNode(6, node5, node4)
node2 = TreeNode(4)
node1 = TreeNode(5, node2, node3)
sol = Solution()
print(sol.isValidBST(node1))
