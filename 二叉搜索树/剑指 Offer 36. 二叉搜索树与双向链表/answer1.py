# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，中序遍历


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None

        def dfs(cur):
            if cur.left:
                dfs(cur.left)
            self.pre.right = cur
            cur.left = self.pre
            self.pre = cur
            if cur.right:
                dfs(cur.right)

        head = Node(0)
        self.pre = head
        dfs(root)
        self.pre.right = head.right
        head.right.left = self.pre
        return head.right
