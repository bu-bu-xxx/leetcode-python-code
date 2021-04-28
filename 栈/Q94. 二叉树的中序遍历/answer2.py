# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 递归是系统自动生成栈，实现迭代
# 手动实现迭代

class Solution:
    def inorderTraversal(self, root):
        result = []
        stack = []
        while root or stack:
            if root:  # 遍历左边
                stack.append(root)
                root = root.left
            else:  # root空，左边不存在，返回栈顶，读数值，遍历右边
                temp = stack.pop()
                result.append(temp.val)
                root = temp.right
        return result
