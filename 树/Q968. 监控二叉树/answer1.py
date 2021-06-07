# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，后序遍历，定义一种安装方法
# 后序遍历，先看left，right状态，然后返回当前点状态
# 返回2表示当前点装监控，1表示子节点有监控，0表示子子节点有监控
# 左右节点中有一个为0则需要装监控
from 树.TreeNode.TreeNode import TreeNode, TreeToList, ListToTree


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        res = [0]

        def dfs(node):
            if node is None:
                return 1
            left_tag = dfs(node.left)
            right_tag = dfs(node.right)
            # 装监控
            if left_tag == 0 or right_tag == 0:
                res[0] += 1
                return 2
            # 调整
            return max(left_tag, right_tag) - 1

        if dfs(root) == 0:
            res[0] += 1
        return res[0]


if __name__ == '__main__':
    try1 = Solution()
    null = None
    root1 = [0, 0, null, 0, 0]
    root1 = ListToTree(root1)
    print(try1.minCameraCover(root1))
