# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，树->图
# 以target为根节点，画图


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
from typing import List

from 树.TreeNode.TreeNode import TreeNode


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = collections.defaultdict(list)
        queue = collections.deque([root])
        while queue:
            tmp = queue.popleft()
            if tmp.left:
                queue.append(tmp.left)
                graph[tmp.val].append(tmp.left.val)
                graph[tmp.left.val].append(tmp.val)
            if tmp.right:
                queue.append(tmp.right)
                graph[tmp.val].append(tmp.right.val)
                graph[tmp.right.val].append(tmp.val)

        # 图搜索
        queue = collections.deque()
        queue.append((target.val, float('inf')))
        row = 1
        while queue:
            for _ in range(len(queue)):
                tmp, father = queue.popleft()
                for nex in graph[tmp]:
                    if nex != father:
                        queue.append((nex, tmp))
            if row == k:
                return [val for val, fat in queue]
            row += 1

        if k == 0:
            return [target.val]
        return []
