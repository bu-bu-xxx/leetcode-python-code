# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 迭代法，用栈迭代

# 1循环，有左节点则左节点进栈
# 2左节点为空，出栈，如果右节点为空，不存，直到存了右节点，回1
# 3每次存节点，打印该值

class Solution:
    def preorderTraversal(self, root):
        if not root:
            return []

        stack = []
        res = []
        while root or stack:
            while root:
                stack.append(root)
                res.append(root.val)
                root = root.left
            temp = stack.pop()
            root = temp.right

        return res
