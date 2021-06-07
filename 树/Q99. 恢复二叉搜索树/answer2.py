# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，隐式中序遍历，递归
# 二叉搜索树的中序遍历是严格单调递增的
# 显式中序遍历，是指把全部节点中序遍历出来，再找出错误点修改值
# 隐式，是指在递归或者迭代过程中就找出两个点
from 树.TreeNode.TreeNode import TreeNode


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 递归中序遍历
        wrong_node = []  # 两个错误点
        last_node = [TreeNode(float('-inf'))]  # 记录上一个点

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if last_node[0].val >= node.val:
                # 记录第一个错误点
                if len(wrong_node) == 0:
                    wrong_node.append(last_node[0])
                    wrong_node.append(node)
                # 第二个错误点
                else:
                    wrong_node[1] = node
            # 存last_node
            last_node[0] = node
            dfs(node.right)

        # 开始遍历，并修改

        dfs(root)
        wrong_node[0].val, wrong_node[1].val = \
            wrong_node[1].val, wrong_node[0].val


if __name__ == '__main__':
    from 树.TreeNode.TreeNode import TreeNode, TreeToList, ListToTree

    try1 = Solution()
    null = None
    root1 = [3, 1, 4, null, null, 2]
    root1 = ListToTree(root1)
    try1.recoverTree(root1)
    print(TreeToList(root1))
