# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 迭代

# 脑袋懵懵，随便改了两下，发现对了，那就懒得理为什么了

class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []

        res = []
        stack = []
        while root or stack:

            while root:
                stack.append(root)
                root = root.left
                stack.append(None)

            temp = stack.pop()
            if temp is None:
                temp = stack.pop()
                res.append(temp.val)
                stack.append(temp)
                root = temp.right
                if temp.right:
                    stack.append(temp)
                    res.pop()
            else:
                res.append(temp.val)
                root = None

        return res[0::2]







