# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/

# 莫里斯遍历法
# 如果左节点不为空，则把当前节点挂在左节点最右边节点上
# 对左节点继续迭代
# 当左节点为空，返回当前节点值，继续迭代右节点

class Solution:
    def inorderTraversal(self, root):
        result = []
        while root:
            if root.left:
                root_left = root.left
                while root_left.right:
                    root_left = root_left.right
                temp = root
                root_left.right = temp
                root = root.left
                temp.left = None
            else:
                result.append(root.val)
                root = root.right
        return result
