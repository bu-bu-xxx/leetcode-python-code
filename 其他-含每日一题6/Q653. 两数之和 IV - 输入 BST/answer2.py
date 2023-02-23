# encoding:utf-8
# @Author :ZQY


# 参考官方答案，迭代实现中序遍历，双指针
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # 找到左指针
        left = root
        left_stack = []
        while left:
            left_stack.append(left)
            left = left.left

        # 找到右指针
        right = root
        right_stack = []
        while right:
            right_stack.append(right)
            right = right.right

        # 双指针查找
        left = left_stack[-1]
        right = right_stack[-1]
        while left != right:
            if left.val + right.val == k:
                return True
            if left.val + right.val < k:
                left = left_stack.pop()
                tmp = left.right
                while tmp:
                    left_stack.append(tmp)
                    tmp = tmp.left
            else:
                right = right_stack.pop()
                tmp = right.left
                while tmp:
                    right_stack.append(tmp)
                    tmp = tmp.right
        return False
