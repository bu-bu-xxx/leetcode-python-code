# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 评论区答案，自己改
# 因为前序遍历，中序遍历，后序遍历任其二能确定一个二叉树
# 左节点的额前序遍历和右节点后序遍历相反
# 左节点和右节点中序遍历相反

# 这个程序不行，对于节点值相同的无法判断
# 可以加上同一个值是第几个出现
# 本程序是不能满足题目要求的
from 树.TreeNode.TreeNode import TreeNode


class Solution:
    # 前序遍历
    def __init__(self):
        self.res4 = []
        self.res3 = []
        self.res2 = []
        self.res1 = []

    def dfs1(self, Root, res):
        if not Root:
            return
        res.append(Root.val)
        self.dfs1(Root.left, res)
        self.dfs1(Root.right, res)

    # 中序遍历
    def dfs2(self, Root, res):
        if not Root:
            return
        self.dfs2(Root.left, res)
        res.append(Root.val)
        self.dfs2(Root.right, res)

    # 后序遍历
    def dfs3(self, Root, res):
        if not Root:
            return
        self.dfs3(Root.left, res)
        self.dfs3(Root.right, res)
        res.append(Root.val)

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None or (root.left is None and root.right is None):
            return True

        # 比前序、后序遍历
        self.dfs1(root.left, self.res1)
        self.dfs3(root.right, self.res2)
        if self.res1 != self.res2[-1::-1]:
            return False

        # 比中序遍历
        self.dfs2(root.left, self.res3)
        self.dfs2(root.right, self.res4)
        if self.res3 != self.res4[-1::-1]:
            return False

        return True


if __name__ == '__main__':
    try1 = Solution()

    from 树.TreeNode.TreeNode import ListToTree

    root1 = ListToTree([1, 2, 2, 2, None, 2])
    print(try1.isSymmetric(root1))
