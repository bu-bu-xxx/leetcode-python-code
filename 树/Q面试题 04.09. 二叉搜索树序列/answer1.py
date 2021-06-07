# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 题目：https://leetcode-cn.com/problems/bst-sequences-lcci/
# 题目解释：https://leetcode-cn.com/problems/bst-sequences-lcci/solution/ru-he-tong-guo-li-zi-de-chu-jie-by-user5707f/
# 自己做
# 队列queue，存当前遍历的路径cur，下一个可以探索的点path
# 出栈，然后把所有可能的path入栈一遍，并更新path
# path等于空则输出，直到queue为空停止迭代
from typing import List

from 树.TreeNode.TreeNode import TreeNode, TreeToList, ListToTree


class Solution:
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return [[]]
        queue = [[[], [root]]]  # [cur,path]
        res = []
        while queue:
            tmp = queue.pop(0)
            cur = tmp[0]
            path = tmp[1]
            # 当path为空时，存入res
            if not path:
                res.append(cur)
            # 当path不为空时，继续走
            else:
                for i in range(len(path)):
                    path_add = []
                    path_i = path[i]
                    if path_i.left:
                        path_add.append(path_i.left)
                    if path_i.right:
                        path_add.append(path_i.right)
                    queue.append([cur + [path[i].val], path[0:i] + path[i + 1:] + path_add])

        # 输出res
        return res
