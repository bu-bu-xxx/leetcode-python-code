# encoding:utf-8
# @Author :ZQY


# 自己做，简单


from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if not root:
            return res

        def dfs(node):
            for child in node.children:
                dfs(child)
            res.append(node.val)

        dfs(root)
        return res
