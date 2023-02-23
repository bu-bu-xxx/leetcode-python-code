# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 自己做
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        res = 0
        min_val = -10 ** 5

        def dfs(node: Optional[TreeNode]):
            nonlocal res
            if not node:
                return 0, 0, 0
            left_val, left_min, left_max = dfs(node.left)
            right_val, right_min, right_max = dfs(node.right)

            node_min = left_min if node.left else node.val
            node_max = right_max if node.right else node.val

            if left_val == min_val or right_val == min_val \
                    or (node.left and left_max >= node.val) \
                    or (node.right and right_min <= node.val):
                return min_val, 0, 0

            res = max(res, left_val + node.val + right_val)
            return left_val + node.val + right_val, node_min, node_max

        dfs(root)
        return res
