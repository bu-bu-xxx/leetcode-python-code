# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，中序遍历


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from 树.TreeNode.TreeNode import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        pre = float('-inf')
        flag = True

        def dfs(node):
            nonlocal flag, pre
            if node.left:
                dfs(node.left)
                if not flag:
                    return
            if pre >= node.val:
                flag = False
            pre = node.val
            if node.right:
                dfs(node.right)
                if not flag:
                    return

        dfs(root)
        return flag
