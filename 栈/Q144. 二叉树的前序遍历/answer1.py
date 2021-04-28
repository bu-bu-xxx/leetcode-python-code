# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 递归，定义

class Solution:
    def preorderTraversal(self, root):
        if not root:
            return []

        res = []

        def dfs(root):
            if not root:
                return None
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return res
