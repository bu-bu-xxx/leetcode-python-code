# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，递归
# 递归返回结果是这个子树是否满足二叉搜索树
# 操作：先预设上限和下限
# 每次递归一个节点就更新一次上下限，因为子节点会继承父节点的上下限，
# 所以更新父节点的值就行
# 可证明：如果当前节点是父节点的左节点，则当前节点的最小上限是父节点，反之亦然
from 树.TreeNode.TreeNode import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def lowerAndUpper(node, lower=float('-inf'), upper=float('inf')):
            # 当节点为空
            if not node:
                return True

            val = node.val
            # 当前节点不满足
            if val <= lower or val >= upper:
                return False
            # 左右子树不满足
            if lowerAndUpper(node.left, lower, val) is False:
                return False
            if lowerAndUpper(node.right, val, upper) is False:
                return False
            # 都满足时，代表这个子树ok
            return True

        return lowerAndUpper(root)
