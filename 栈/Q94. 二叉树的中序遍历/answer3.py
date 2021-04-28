# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 递归，另一种方法，手动迭代挺难想的

class Solution:
    def inorderTraversal(self, root):
        result = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            temp = stack.pop()
            result.append(temp.val)
            root = temp.right
        return result

