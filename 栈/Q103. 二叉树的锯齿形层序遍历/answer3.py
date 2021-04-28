# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 深度优先：前序，中序，后序
# 用的是前序，递归方法

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        import collections as col
        res = []

        def dfs(root, index):  # 层数index
            if not root:  # 到头返回
                return None
            if len(res) < index:
                res.append(col.deque())
            if index % 2 == 1:  # 奇数层
                res[index - 1].append(root.val)
            else:  # 偶数层
                res[index - 1].appendleft(root.val)
            dfs(root.left, index + 1)
            dfs(root.right, index + 1)

        dfs(root, 1)
        res_list = [list(i) for i in res]
        return res_list
