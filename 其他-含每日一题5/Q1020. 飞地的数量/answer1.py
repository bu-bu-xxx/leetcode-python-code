# encoding:utf-8
# @Author :ZQY


# 自己做，深度优先搜索
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        nex = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(node: tuple):
            i, j = node[0], node[1]
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = 0
                for i_add, j_add in nex:
                    dfs((i_add + i, j_add + j))

        # grid的边界作为根节点
        for x in range(m):
            dfs((x, 0))
            dfs((x, n - 1))
        for y in range(n):
            dfs((0, y))
            dfs((m - 1, y))

        return sum([sum(grid[i]) for i in range(m)])
