# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，递归
# 判断root1和root2为根节点的树是否对称
from 树.TreeNode.TreeNode import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def bfs(root1, root2):
            if root1 is None or root2 is None:
                return root1 == root2
            if root1.val != root2.val:
                return False
            t1 = bfs(root1.left, root2.right)
            t2 = bfs(root1.right, root2.left)
            return t2 and t1

        return bfs(root, root)
