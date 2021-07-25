# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversalDFS(self, root: TreeNode) -> [int]:
        res = []
        self.traversalFuncDFS(root, res)
        return res

    def traversalFuncDFS(self, root: TreeNode, res: [int]):
        if root is None:
            return
        self.traversalFuncDFS(root.left, res)
        res.append(root.val)
        self.traversalFuncDFS(root.right, res)
        return

    def inorderTraversalInteration(self, root: TreeNode) -> [int]: # not BFS just translate DFS
        res = []
        node = root
        nodes = []
        while nodes or node:
            while node is not None:
                nodes.append(node)
                node = node.left
            node = nodes[-1]
            res.append(node.val)
            nodes = nodes[:-1]
            node = node.right
        return res

solve = Solution()
node1 = TreeNode()
node1.val = 1
node2 = TreeNode()
node3 = TreeNode()
node4 = TreeNode()
node5 = TreeNode()
node6 = TreeNode()
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
node2.val = 2
node3.val = 3
node4.val = 4
node5.val = 5
node6.val = 6
print(solve.inorderTraversalInteration(node1))
