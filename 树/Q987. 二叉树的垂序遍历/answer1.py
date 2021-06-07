# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做
# 先标坐标，按列->行->值，升序排序
# 同列同数组，剩下按顺序放进去
from typing import List

from 树.TreeNode.TreeNode import TreeNode, TreeToList, ListToTree


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        point = []  # (列,行,值)

        def dfs(node, row, col):
            if node is None:
                return
            point.append((col, row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)
        res = []
        point = sorted(point)
        column = -100000
        num = -1
        for col, row, val in point:
            if col != column:
                num += 1
                column = col
                res.append([val])
            else:
                res[num].append(val)
        return res


if __name__ == '__main__':
    try1 = Solution()
    null = None

    root1 = [3, 9, 20, null, null, 15, 7]
    root1 = ListToTree(root1)
    print(try1.verticalTraversal(root1))

    root2 = [1, 2, 3, 4, 6, 5, 7]
    root2 = ListToTree(root2)
    print(try1.verticalTraversal(root2))
