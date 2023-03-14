# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# Q4为该题变种

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from 树.TreeNode.TreeNode import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -10**10

        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
            left_sum = max(dfs(node.left),0)
            right_sum = max(dfs(node.right),0)
            max_sum = max(max_sum, left_sum + right_sum + node.val)
            return max(left_sum, right_sum, 0) + node.val

        dfs(root)
        return max_sum
