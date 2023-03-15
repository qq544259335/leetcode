from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: [TreeNode]) -> [int]:
        # obviously level order traversal
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            row_max = float('-inf')
            for _ in range(size):
                node = queue.popleft()
                if node:
                    row_max = max(row_max, node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if row_max != float('-inf'):
                res.append(row_max)
        return res

