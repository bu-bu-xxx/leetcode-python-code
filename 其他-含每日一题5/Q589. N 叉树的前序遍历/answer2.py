# encoding:utf-8
# @Author :ZQY


# 简单题，迭代
import collections
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        queue = collections.deque([root])
        res = []
        while queue:
            node = queue.popleft()
            res.append(node.val)
            queue = collections.deque(node.children) + queue
        return res
