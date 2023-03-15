# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = 0
    depth = 0

    def maxDepth(self, root: TreeNode) -> int:
        def traverse(node: TreeNode):
            if not node:
                self.res = max(self.res, self.depth)
                return
            self.depth += 1
            traverse(node.left)
            traverse(node.right)
            self.depth -= 1

        traverse(root)
        return self.res

    def maxDepthRecursion(self, root: TreeNode) -> int:
        def recursion(node: TreeNode):
            if not node:
                return 0
            return max(recursion(node.left), recursion(node.right)) + 1
        return recursion(root)