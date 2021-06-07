# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，深度优先遍历，递归
# 输入当前节点，父节点的序列串，路径和
# 然后加上当前节点更新序列串和路径和
# 如果有子节点则递归子节点
# 路径和满足条件的，加入到全局变量中存储
from 树.TreeNode.TreeNode import TreeNode


class Solution:

    def pathSum(self, root: TreeNode, targetSum: int):
        result = []
        if not root:
            return result
        road = []

        def roadSum(node, sum_val):
            road.append(node.val)
            sum_val += node.val
            if sum_val == targetSum and node.left is None and node.right is None:
                result.append(road[:])
            if node.left:
                roadSum(node.left, sum_val)
            if node.right:
                roadSum(node.right, sum_val)
            road.pop()

        roadSum(root, 0)
        return result


if __name__ == '__main__':
    from 树.TreeNode.TreeNode import TreeNode, TreeToList, ListToTree

    try1 = Solution()
    null = None
    root1 = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1]
    root1 = ListToTree(root1)
    targetSum1 = 22
    print(try1.pathSum(root1, targetSum1))
