# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    res = float('-inf')

    def maxPathSum(self, root: [TreeNode]) -> int:
        def get_max_linked_to_this_node(node: TreeNode) -> int:
            if not node:
                return 0
            left_max = get_max_linked_to_this_node(node.left)
            right_max = get_max_linked_to_this_node(node.right)
            print(node.val, self.res, left_max, right_max)
            self.res = max(self.res, left_max + node.val, right_max + node.val, left_max + right_max + node.val,
                           node.val)
            return max(left_max + node.val, right_max + node.val, node.val)

        get_max_linked_to_this_node(root)
        return self.res
