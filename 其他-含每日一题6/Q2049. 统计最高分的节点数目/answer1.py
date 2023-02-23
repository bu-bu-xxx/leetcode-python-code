# encoding:utf-8
# @Author :ZQY


# 自己做，深度优先搜索
from typing import List


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        children = [[] for _ in range(n)]

        # 生成子节点
        for ch in range(1, n):
            children[parents[ch]].append(ch)

        # 后序遍历
        points_max = 0
        count = 0

        def dfs(node):
            nonlocal points_max, count
            left_len, right_len = 0, 0
            for i, child in enumerate(children[node]):
                if i == 0:
                    left_len = dfs(child)
                if i == 1:
                    right_len = dfs(child)
            points = 1
            points *= left_len if left_len > 0 else 1
            points *= right_len if right_len > 0 else 1
            points *= n - left_len - right_len - 1 if n - left_len - right_len - 1 > 0 else 1
            if points > points_max:
                count = 1
                points_max = points
            elif points == points_max:
                count += 1

            return left_len + right_len + 1

        dfs(0)
        return count
