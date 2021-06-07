# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，隐式中序遍历，迭代
# 二叉搜索树的中序遍历是严格单调递增的
# 第一种情况，两个错误点连着
# 第二种情况，不连着
# 备注：迭代和递归原理一样，复杂度基本一样
from 树.TreeNode.TreeNode import TreeNode


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        stack = []
        wrong_node = [None, None]
        last_node = [TreeNode(float('-inf'))]
        while root or stack:
            # 左节点
            if root:
                stack.append(root)
                root = root.left
            # 出栈，找错误点
            else:
                temp = stack.pop()
                if last_node[0].val >= temp.val:
                    # 第一个错误点
                    if wrong_node[0] is None:
                        wrong_node[0] = last_node[0]
                        wrong_node[1] = temp
                    # 第二个错误点
                    else:
                        wrong_node[1] = temp
                last_node[0] = temp
                # 右节点
                root = temp.right

        # 换val
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
