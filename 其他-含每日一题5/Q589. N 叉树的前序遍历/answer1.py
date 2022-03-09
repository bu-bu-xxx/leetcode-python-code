# encoding:utf-8
# @Author :ZQY


# 简单题，递归
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res

        def dfs(node):
            res.append(node.val)
            for nex in node.children:
                dfs(nex)

        dfs(root)
        return res
