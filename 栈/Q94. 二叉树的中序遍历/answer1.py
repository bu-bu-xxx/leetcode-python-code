# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 递归遍历
# 中序遍历：左-打印-右

class Solution:
    def inorderTraversal(self, root):
        result = []
        def diedai(root):
            if not root:
                return None
            diedai(root.left)
            result.append(root.val)
            diedai(root.right)
        diedai(root)
        return result





