# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def preorderTraversal(self, root: [TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        r = []
        while q:
            cur = q.pop()
            if cur:
                r.append(cur.val)
                q.append(cur.right if cur.right else None)
                q.append(cur.left if cur.left else None)
        return r

    def preorderTraversalRecursion(self, root: [TreeNode]) -> List[int]:
        r = []
        def rec(node: TreeNode):
            r.append(node.val)
            if node.left:
                rec(node.left)
            if node.right:
                rec(node.right)
        rec(root)
        return r