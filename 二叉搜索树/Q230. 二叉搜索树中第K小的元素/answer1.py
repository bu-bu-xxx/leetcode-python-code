# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，二叉搜索树中序遍历


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from 树.TreeNode.TreeNode import TreeNode


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count = 0
        flag = False
        res = 0

        def find(node):
            nonlocal count, flag, res
            if node.left:
                find(node.left)
                if flag:
                    return
            count += 1
            if count == k:
                res = node.val
                flag = True
                return

            if node.right:
                find(node.right)
                if flag:
                    return

        find(root)
        return res
