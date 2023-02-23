# encoding:utf-8
# @Author :ZQY


# 自己做，递归

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def tree2str(self, t):
        if not t:
            return ""
        if not t.left and not t.right:
            return str(t.val)
        result = str(t.val)
        if t.left:
            result += "(" + self.tree2str(t.left) + ")"
        else:
            result += "()"
        if t.right:
            result += "(" + self.tree2str(t.right) + ")"
        return result
