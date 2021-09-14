# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> [[int]]:
        res = []
        nodesList = [root]
        while nodesList:
            temp = []
            length = len(nodesList)
            for i in range(length):
                node = nodesList.pop(0)
                if node:
                    nodesList.append(node.left)
                    nodesList.append(node.right)
                    temp.append(node.val)
            if temp:
                res.append(temp)
        return res


node4 = TreeNode(4)
node3 = TreeNode(3, node4)
node2 = TreeNode(2)
node1 = TreeNode(1, node2, node3)
sol = Solution()
print(sol.levelOrder(node1))
