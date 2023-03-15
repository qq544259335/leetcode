# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: [TreeNode]) -> int:
        nums = []
        def dfs(node:root) ->int:
            nums.append(str(node.val))
            temp_sum = 0
            if not node.right and not node.left:
                temp_sum += int("".join(nums)) if len(nums) > 0 else 0
                nums.pop(-1)
            else:
                if node.left:
                    temp_sum += dfs(node.left)
                if node.right:
                    temp_sum += dfs(node.right)
                nums.pop(-1)
            return temp_sum
        return dfs(root)
