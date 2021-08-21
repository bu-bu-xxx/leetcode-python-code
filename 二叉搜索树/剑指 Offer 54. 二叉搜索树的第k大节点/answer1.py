# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，中序遍历
# ez


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from 树.TreeNode.TreeNode import TreeNode


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        times = 0
        res = [0]

        def count(node):
            nonlocal times
            if node.right:
                count(node.right)

            times += 1
            if times == k:
                res[0] = node.val
            if node.left:
                count(node.left)

        count(root)
        return res[0]


if __name__ == "__main__":
    try1 = Solution()
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node2.left = node1
    node2.right = node3
    print(try1.kthLargest(node2, 3))
