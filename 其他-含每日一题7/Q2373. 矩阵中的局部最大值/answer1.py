# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 自己做，简单
from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res_grid = [[0] * (n - 2) for _ in range(n - 2)]
        for i in range(n - 2):
            for j in range(n - 2):
                res_grid[i][j] = max([max(s[j:j + 3]) for s in grid[i:i + 3]])
        return res_grid
