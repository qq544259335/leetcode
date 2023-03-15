# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = 0

    def diameterOfBinaryTree(self, root: [TreeNode]) -> int:
        def max_depth(root: TreeNode):
            if not root:
                return 0
            left_max = max_depth(root.left)
            right_max = max_depth(root.right)
            self.res = max(self.res, left_max + right_max)
            return max(left_max, right_max) + 1
        max_depth(root)
        return self.res
