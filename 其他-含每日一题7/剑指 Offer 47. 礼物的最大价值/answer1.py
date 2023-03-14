# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 自己做，动态规划
from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                tmp = grid[i][j]
                for i_add, j_add in [(-1, 0), (0, -1)]:
                    i_pre, j_pre = i + i_add, j + j_add
                    if 0 <= i_pre < m and 0 <= j_pre < n:
                        tmp = max(tmp, grid[i][j] + grid[i_pre][j_pre])
                grid[i][j] = tmp

        return grid[-1][-1]
