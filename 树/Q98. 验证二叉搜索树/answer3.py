# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，中序遍历，自己写
# 可证明：二叉搜索树的充分必要条件是中序遍历严格单调递增
# 官方答案是中序遍历迭代去修改，我是用递归修改
from 树.TreeNode.TreeNode import TreeNode


class Solution:
    def __init__(self):
        self.last_val = float('-inf')

    def isValidBST(self, root: TreeNode) -> bool:
        # 中序遍历
        self.last_val = float('-inf')

        def dfs(node):
            if not node:
                return True
            if dfs(node.left) is False:
                return False
            if (val := node.val) > self.last_val:
                self.last_val = val
            else:
                return False
            if dfs(node.right) is False:
                return False
            return True

        return dfs(root)


if __name__ == '__main__':
    from 树.TreeNode.TreeNode import TreeNode, TreeToList, ListToTree

    try1 = Solution()
    root1 = ListToTree([2, 1, 3])
    print(try1.isValidBST(root1))
