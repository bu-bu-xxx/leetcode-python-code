# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 理解错题目意思了，下面计算的是，只能搜索子节点的最大连续路径和


# 自己做，递归，深度优先搜索
# 递归:空节点返回，非空则更新当前路径，并找到最大的路径和
# 找给定路线的最大路径的起始和末尾点，计算从头开始的阶和，最大减最小即可
from 树.TreeNode.TreeNode import TreeNode


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        sum_road_val = []

        # 给定根节点到当前节点的阶和列表，找最大路径
        # 计算当前阶和-min(前i-1个阶和,0)=最大路径和
        # 迭代输入当前阶和最小值
        # return当前最大路径和
        def dfs(node, min_val):
            # 根节点
            if not sum_road_val:
                sum_road_val.append(node.val)
                max1 = node.val
                min_val = min(min_val, sum_road_val[-1])
            # 其他节点
            else:
                sum_road_val.append(sum_road_val[-1] + node.val)
                max1 = sum_road_val[-1] - min(min_val, 0)
                min_val = min(min_val, sum_road_val[-1])
            # 子节点
            if node.left is not None:
                max2 = dfs(node.left, min_val)
            else:
                max2 = float('-inf')
            if node.right is not None:
                max3 = dfs(node.right, min_val)
            else:
                max3 = float('-inf')
            # 出栈sum_road_val
            sum_road_val.pop()
            return max(max1, max2, max3)

        return dfs(root, float('inf'))


if __name__ == '__main__':
    from 树.TreeNode.TreeNode import TreeNode, TreeToList, ListToTree

    try1 = Solution()
    root1 = [1, 2, 3]
    root1 = ListToTree(root1)
    print(try1.maxPathSum(root1))
