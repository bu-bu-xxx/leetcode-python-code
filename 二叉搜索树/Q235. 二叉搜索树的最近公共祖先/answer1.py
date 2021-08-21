# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，二叉树特性


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from 树.TreeNode.TreeNode import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while max(p.val, q.val) < root.val or min(p.val, q.val) > root.val:
            if max(p.val, q.val) < root.val:
                root = root.left
            else:
                root = root.right

        return root
