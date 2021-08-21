# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，广度优先搜索


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from typing import List

from 树.TreeNode.TreeNode import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        queue = collections.deque()
        n = len(nums)
        root = TreeNode()
        queue.append([root, (0, n - 1)])

        while queue:
            tmp = queue.popleft()
            mid = (tmp[1][0] + tmp[1][1]) // 2
            tmp[0].val = nums[mid]
            if tmp[1][0] < mid:
                new = TreeNode()
                tmp[0].left = new
                queue.append([new, (tmp[1][0], mid - 1)])
            if tmp[1][1] > mid:
                new = TreeNode()
                tmp[0].right = new
                queue.append([new, (mid + 1, tmp[1][1])])

        return root
