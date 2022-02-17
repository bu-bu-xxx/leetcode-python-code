# encoding:utf-8
# @Author :ZQY


# 自己做，广度优先搜索
import collections
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        nex = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = collections.deque()

        # grid的边界作为根节点
        for x in range(m):
            if grid[x][0] == 1:
                queue.append((x, 0))
                grid[x][0] = 0
            if grid[x][n - 1] == 1:
                queue.append((x, n - 1))
                grid[x][n - 1] = 0
        for y in range(n):
            if grid[0][y] == 1:
                queue.append((0, y))
                grid[0][y] = 0
            if grid[m - 1][y] == 1:
                queue.append((m - 1, y))
                grid[m - 1][y] = 0

        while queue:
            node = queue.popleft()
            i, j = node[0], node[1]
            for i_add, j_add in nex:
                nex_i, nex_j = i_add + i, j_add + j
                if 0 <= nex_i < m and 0 <= nex_j < n and grid[nex_i][nex_j] == 1:
                    grid[nex_i][nex_j] = 0
                    queue.append((nex_i, nex_j))

        return sum([sum(grid[i]) for i in range(m)])
