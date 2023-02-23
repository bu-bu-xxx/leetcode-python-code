# encoding:utf-8
# @Author :ZQY


# 自己做，优先搜索，哈希表
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hash_set = set()

        def dfs(node):
            if node.val in hash_set:
                return True
            hash_set.add(k - node.val)
            if node.left and dfs(node.left):
                return True
            if node.right and dfs(node.right):
                return True
            return False

        return dfs(root)
