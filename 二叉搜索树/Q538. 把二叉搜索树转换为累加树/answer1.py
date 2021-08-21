# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，二叉搜索树，中序遍历


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from 树.TreeNode.TreeNode import TreeNode


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        sum_val = 0

        def dfs(node):
            nonlocal sum_val
            if node.right:
                dfs(node.right)
            sum_val += node.val
            node.val = sum_val
            if node.left:
                dfs(node.left)

        dfs(root)
        return root
