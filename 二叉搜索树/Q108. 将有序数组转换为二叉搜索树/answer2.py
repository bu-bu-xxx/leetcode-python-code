# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，前序遍历


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from 树.TreeNode.TreeNode import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def dp(left, right):
            mid = (left + right) // 2
            new = TreeNode(val=nums[mid])
            if left < mid:
                new.left = dp(left, mid - 1)
            if right > mid:
                new.right = dp(mid + 1, right)
            return new

        return dp(0, len(nums) - 1)
