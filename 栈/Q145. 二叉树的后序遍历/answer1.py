# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 递归法，定义

class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []

        res = []

        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)

        dfs(root)
        return res
