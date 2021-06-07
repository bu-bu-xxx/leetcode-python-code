# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，递归
# 每次递归判断，是否大于左子树最大值，小于右子树最小值，不满足返回False
# 如果满足返回当前树的最大值和最小值
# 备注：这个做的复杂度都不好，应该换一种递归判定方法
from 树.TreeNode.TreeNode import TreeNode


class Solution:
    def __init__(self):
        self.flag = True

    def isValidBST(self, root: TreeNode) -> bool:
        self.flag = True

        def dfs(root1):
            # 当不满足flag时
            if self.flag is False:
                return 1, 1
            # 当当前节点为空时
            if not root1:
                return None, None
            # 当子树都不空时
            left_val = dfs(root1.left)
            right_val = dfs(root1.right)
            # 判断flag
            if left_val[1] is not None and left_val[1] >= root1.val:
                self.flag = False
                return 1, 1
            if right_val[0] is not None and right_val[0] <= root1.val:
                self.flag = False
                return 1, 1
            # 返回最大值最小值
            min_val = min(root1.val, left_val[0]) if left_val[0] is not None else root1.val
            max_val = max(root1.val, right_val[1]) if right_val[1] is not None else root1.val
            return min_val, max_val

        dfs(root)
        return self.flag


if __name__ == '__main__':
    from 树.TreeNode.TreeNode import TreeNode, TreeToList, ListToTree

    try1 = Solution()
    r = ListToTree([32, 26, 47, 19, None, None, 56, None, 27])
    print(try1.isValidBST(r))
