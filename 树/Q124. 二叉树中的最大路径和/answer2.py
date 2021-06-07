# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，递归
# 递归返回当前节点max(当前节点开始最大路径和,0)
# return有三种可能，1.当前节点+左树，2.当前节点+右树，3.空
# 每次递归更新一次全局变量，最大路径和
from 树.TreeNode.TreeNode import TreeNode


class Solution:
    def __init__(self):
        self.max_val = float('-inf')

    def maxPathSum(self, root: TreeNode):
        def dfs(node):
            # 到头，空节点
            if node is None:
                return 0
            # 正常节点
            left_val = dfs(node.left)
            right_val = dfs(node.right)
            # 更新最大路径和
            self.max_val = max(self.max_val, left_val + right_val + node.val)
            # return
            return max(0, node.val + left_val, node.val + right_val)

        dfs(root)
        return self.max_val


if __name__ == '__main__':
    from 树.TreeNode.TreeNode import TreeNode, TreeToList, ListToTree

    try1 = Solution()
    root1 = [1, 2, 3]
    root1 = ListToTree(root1)
    print(try1.maxPathSum(root1))
