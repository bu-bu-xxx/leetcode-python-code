# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，深度优先搜索
from 树.TreeNode.TreeNode import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return 1 + max(left_height, right_height)


if __name__ == '__main__':
    from 树.TreeNode.TreeNode import ListToTree

    try1 = Solution()

    root1 = ListToTree([3, 9, 20, None, None, 15, 7])
    print(try1.maxDepth(root1))
