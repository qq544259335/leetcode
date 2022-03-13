# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: [[int]]) -> [TreeNode]:
        node_dict = {}
        parent_dict = {}
        for p, c, l in descriptions:
            if p not in node_dict:
                p_node = TreeNode(p)
                node_dict[p] = p_node
            else:
                p_node = node_dict[p]
            if p not in parent_dict:
                parent_dict[p] = []
            if c not in parent_dict:
                parent_dict[c] = []
            if c not in node_dict:
                c_node = TreeNode(c)
                node_dict[c] = c_node
            else:
                c_node = node_dict[c]
            if l == 1:
                p_node.left = c_node
            else:
                p_node.right = c_node
            parent_dict[c].append(p)
        for k, v in parent_dict.items():
            if not v:
                return node_dict[k]
