# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，深度优先搜索
# 用递归，当前最小深度=min(左子树最小深度,右子树最小深度)+1
# 左右节点都为空的才是叶子
# 碰到空的点返回0
from 树.TreeNode.TreeNode import TreeNode


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_min = self.minDepth(root.left)
        right_min = self.minDepth(root.right)
        # 单边子树空，另一边不空，返回不空的子树深度+1
        if (left_min == 0 and right_min != 0) or \
                (left_min != 0 and right_min == 0):
            return max(left_min, right_min) + 1
        # 当两个子树都非空
        return min(left_min, right_min) + 1


if __name__ == '__main__':
    from 树.TreeNode.TreeNode import TreeNode, TreeToList, ListToTree

    try1 = Solution()
    root1 = [3, 9, 20, None, None, 15, 7]
    root1 = ListToTree(root1)
    print(try1.minDepth(root1))
