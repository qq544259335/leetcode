class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root:
            queue = [root]
            depth = 1
            while queue:
                length = len(queue)
                for i in range(length):
                    cur = queue.pop(0)
                    if cur.left is None and cur.right is None:
                        return depth
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                depth += 1
        else:
            return 0
